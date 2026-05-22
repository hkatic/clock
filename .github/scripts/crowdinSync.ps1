#!/usr/bin/env pwsh
$ErrorActionPreference = 'Stop'

# Git configuration for automated commits
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

$rawAddonId = $env:ADDON_ID
if ([string]::IsNullOrWhiteSpace($rawAddonId)) {
    Write-Error "Failed to get addon ID."
    exit 1
}
$addonId = $rawAddonId.Trim()

# --- STEP 1: PREPARATION AND SOURCE UPDATE ---

$xliffFile = "./$addonId.xliff"
$mdFile = "./readme.md"

if (Test-Path $mdFile) {
    if (Test-Path $xliffFile) {
        $tempXliff = [System.IO.Path]::GetTempFileName()
        try {
            Copy-Item "$addonId.xliff" $tempXliff -Force
            Write-Host "DEBUG: Updating XLIFF source based on readme.md..."
            uv run .github/scripts/markdownTranslate.py updateXliff -m $mdFile -x $tempXliff -o $xliffFile
        } finally {
            if (Test-Path $tempXliff) {
                Remove-Item $tempXliff -Force
            }
        }
    } else {
        Write-Host "DEBUG: XLIFF template not found. Creating new one from readme.md..."
        uv run .github/scripts/markdownTranslate.py generateXliff -m $mdFile -o $xliffFile
    }
}

# Update POT file (addon interface)
uv run scons pot
$potFile = "$addonId.pot"

# --- STEP 2: UPLOAD SOURCES TO CROWDIN ---

if (Test-Path $potFile) {
    Write-Host "DEBUG: Uploading updated POT source to Crowdin..."
    ./l10nUtil.exe uploadSourceFile "$potFile" -c $env:L10N_UTIL_CONFIG
}

if (Test-Path $xliffFile) {
    Write-Host "DEBUG: Uploading updated XLIFF source to Crowdin..."
    ./l10nUtil.exe uploadSourceFile "$xliffFile" -c $env:L10N_UTIL_CONFIG
    git add "$xliffFile"
    git diff --staged --quiet
    if ($LASTEXITCODE -ne 0) {
        git commit -m "Update $xliffFile for $addonId"
        git push
    }
}

# --- STEP 3: EXPORT AND PROCESS TRANSLATIONS ---

Write-Host "DEBUG: Exporting translations from Crowdin..."
./l10nUtil.exe exportTranslations -o _addonL10n -c $env:L10N_UTIL_CONFIG

# Ensure base directories exist
New-Item -ItemType Directory -Force -Path addon/locale | Out-Null
New-Item -ItemType Directory -Force -Path addon/doc | Out-Null

# Load language mappings for Crowdin API calls
$languageMappings = Get-Content -Raw ".github/scripts/languageMappings.json" | ConvertFrom-Json

foreach ($dir in Get-ChildItem -Path "_addonL10n/$addonId" -Directory) {
    $langCode = $dir.Name

    if ($langCode -eq "en") { continue }

    # --- Identify codes
    $crowdinLang = $null

    # Use the ."variable" syntax to correctly read the PSCustomObject from JSON
    if ($languageMappings.PSObject.Properties.Name -contains $langCode) {
        $crowdinLang = $languageMappings."$langCode"
    }

    # Fallback: If no mapping is found, replace underscores with dashes for Crowdin compatibility
    if (-not $crowdinLang) {
        $crowdinLang = $langCode.Replace('_', '-')
    }

    # The $langCode (folder name from Crowdin) represents the local repository language code.
    # It matches the NVDA directory structure, so no extra mapping is needed.
    Write-Host "--- Processing Language: $langCode (Crowdin: $crowdinLang) ---" -ForegroundColor Cyan

    # Paths
    $remoteMd = Join-Path $dir.FullName "$addonId.md"
    $remoteXliff = Join-Path $dir.FullName "$addonId.xliff"
    $remotePo = Join-Path $dir.FullName "$addonId.po"
    $localMdDir = "addon/doc/$langCode"
    $localMd = "$localMdDir/readme.md"
    $localPoPath = "addon/locale/$langCode/LC_MESSAGES/nvda.po"

    # --- 3.1 PO FILE PROCESSING ---
    $poImported = $false
    if (Test-Path $remotePo) {
        Write-Host "DEBUG: Checking Remote PO progress for $crowdinLang..."
        uv run python .github/scripts/checkTranslation.py "$addonId.po" $crowdinLang
        if ($LASTEXITCODE -eq 0) {
            Write-Host "SUCCESS: Remote PO is valid. Importing to $localPoPath"
            New-Item -ItemType Directory -Force -Path (Split-Path $localPoPath) | Out-Null
            Move-Item $remotePo $localPoPath -Force
            $poImported = $true
        } else {
            Write-Host "WARNING: Remote PO progress is below threshold."
        }
    }

    if (-not $poImported -and (Test-Path $localPoPath)) {
        Write-Host "ACTION: Uploading local legacy PO to Crowdin ($crowdinLang) as fallback."
        ./l10nUtil.exe uploadTranslationFile $crowdinLang "$addonId.po" $localPoPath -c $env:L10N_UTIL_CONFIG
    }

    # --- 3.2 DOCUMENTATION PROCESSING (MD & XLIFF) ---
    $scoreMd = 0.0
    $scoreXliff = 0.0

    if (Test-Path $remoteMd) {
        Write-Host "DEBUG: Evaluating Remote Markdown score..."
        $res = uv run python .github/scripts/checkTranslation.py "$addonId.md" $crowdinLang
        $scoreMd = [double]($res | Select-String "mdScore=").ToString().Split("=")[1]
    } else {
        Write-Host "DEBUG: No remote Markdown file found for this language."
    }

    if (Test-Path $remoteXliff) {
        Write-Host "DEBUG: Evaluating Remote XLIFF score..."
        $res = uv run python .github/scripts/checkTranslation.py "$addonId.xliff" $crowdinLang
        $scoreXliff = [double]($res | Select-String "xliffScore=").ToString().Split("=")[1]
    } else {
        Write-Host "DEBUG: No remote XLIFF file found for this language."
    }

    Write-Host "DEBUG: Comparison Scores -> MD: $scoreMd | XLIFF: $scoreXliff"

    $threshold = 0.5
    $docImported = $false

    if ($scoreXliff -gt $threshold -or $scoreMd -gt $threshold) {
        if (!(Test-Path $localMdDir)) { New-Item -ItemType Directory -Force -Path $localMdDir | Out-Null }

        if ($scoreXliff -ge $scoreMd) {
            Write-Host "SUCCESS: XLIFF is better or equal. Converting XLIFF to local MD ($langCode)..."
            ./l10nUtil.exe xliff2md $remoteXliff $localMd
            $docImported = $true
        } else {
            Write-Host "SUCCESS: Markdown is better. Importing Remote MD to local ($langCode)..."
            Move-Item $remoteMd $localMd -Force
            $docImported = $true
        }
    } else {
        Write-Host "WARNING: Both remote MD and XLIFF scores are below threshold ($threshold)."
    }

    if (-not $docImported -and (Test-Path $localMd)) {
        Write-Host "ACTION: Documentation quality too low. Uploading local MD to Crowdin ($crowdinLang) as fallback."
        ./l10nUtil.exe uploadTranslationFile $crowdinLang "$addonId.md" $localMd -c $env:L10N_UTIL_CONFIG
    }
}

# --- STEP 4: COMMIT UPDATED TRANSLATIONS ---

git add addon/locale addon/doc
git diff --staged --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "Update translations for $addonId from Crowdin (Automatic Sync)"
    $branch = $env:downloadTranslationsBranch
    git push -f origin "HEAD:$branch"
    Write-Host "SUCCESS: Translations committed and pushed."
} else {
    Write-Host "DEBUG: No changes in translations to commit."
}
