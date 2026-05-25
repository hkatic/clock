# Ur og kalender for NVDA

- Authors: Hrvoje Katić, Abdel and NVDA contributors
- Download [stabil version][1]
- NVDA-kompatibilitet: 2019.3 og nyere
- NVDA compatibility: 2019.3 and later

Denne tilføjelse tilføjer avancerede ur, alarm, tidtagning  og
kalenderfunktionalitet til NVDA.

You can configure NVDA to announce time and date in formats other than what Windows provides by default. Additionally, you can obtain the current day, week number, as well as the remaining days before the end of the current year, and you can also set automatic time announcement on specified interval. There's also a stopwatch and Alarm timer features built-in to the add-on that lets you time your tasks, such as copying files, installing programs, or cooking meals.

Bemærkninger:

- if you install the add-on as an update, during the installation process, the wizard detects if the old configuration is compatible with the new one and offers to correct it before installing, then you'll just have to validate the OK button to confirm that.
- I Windows 10 og nyere kan du bruge appen Alarmer og ur til at administrere
  stopur og timere.

## Tastaturkommandoer

- NVDA+F12: Få den aktuelle tid oplyst.
- NVDA+F12 trykket hurtigt to gange: få aktuel dato
- NVDA+F12 trykket tre gange hurtigt: Oplyser den aktuelle dag, ugenummeret,
  det aktuelle år og de resterende dage før årets udgang.
- NVDA+Shift+F12: indtast urlag

## Ikke-tildelte kommandoer

The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands. To do so, open NVDA menu, Preferences, then Input Gestures. Expand Clock category, then locate unassigned commands from the list below and select "Add", then enter the gesture you wish to use.

- Elapsed and remaining time before the next alarm. pressing this gesture twice quickly will cancel the next alarm.
- Stop afspilning af den aktuelle alarmlyd
- Vis dialog til indstilling af alarmer
- Show layered commands (keys to be pressed after NVDA+Shift+F12).

## Lagrede kommandoer

For at bruge lagrede kommandoer skal du trykke på NVDA+Skift+F12 efterfulgt
af en af følgende taster:

- S: Starter, nulstiller eller stopper stopuret
- R: Nulstiller stopuret til 0 uden at genstarte det
- A: Giver den resterende og forløbet tid før den næste alarm
- T: Åbner dialogen til indstilling af alarmer.
- C: Annuller den næste alarm
- Mellemrum: Udtaler nuværende stopur eller nedtælling
- P: Hvis en alarm er for lang, kan du stoppe den via dette tastetryk.
- H: Liste over alle lagdelte kommandoer (Hjælp)

## Konfiguration og brug

For at konfigurere urfunktionaliteten skal du åbne NvDA-menuen, Opsætning og
derefter Indstillinger og konfigurere følgende muligheder fra
indstillingskategorien Ur:

- Visningsformat for klokkeslæt og dato: Brug disse kombinationsbokse til at
  konfigurere, hvordan NVDA vil annoncere klokkeslæt og dato, når du trykker
  på NVDA+F12 en eller to gange hurtigt.
- Interval: choose the time announcement interval from this combo box (off, every 10 minutes, 15 minutes, 30 minutes, or every hour).
- Tidsannoncering (aktiveret, hvis interval ikke er slået fra): vælg mellem
  tale og lyd, kun lyd eller kun tale.
- Urets ringelyd  (aktiveret, hvis interval ikke er slået fra): vælg lyden
  for uret.
- Checkboxe "Stilletimer" (kun synlig, hvis muligheden "Fra" ikke er valgt i
  boksen) giver dig mulighed for at konfigurere tidsintervallet, hvor den
  automatiske tidsannoncering ikke skal forekomme.
  - Intermediate minutes chime sound (enabled if "Separate hour and intermediate minute chimes" is checked): Select the clock chime sound specifically for intermediate minutes.
- Tidsformat for stilletimer (aktiveret, hvis stilletimer er aktiveret):
  vælg, hvordan indstillingerne for stilletimer præsenteres (12-timers eller
  24-timers format).
- Stilletimers start- og sluttidspunkter: Vælg time- og minutinterval for
  stilletimer fra combo boxe for timer og minutter.
- Quiet hours start and end times: select hour and minute range for quiet hours from hours and minutes combo boxes.

To schedule alarms, open NVDA menu, Tools, then select Schedule Alarms. The dialog contents include:

- Alarmens varighed i: Vælg alarm/timer-varighed mellem timer, minutter og
  sekunder.
- Varighed: Indtast alarmvarigheden som anvist ovenfor.
- Alarmlyd: Vælg den alarmlyd, der skal afspilles.
- Knapper til pause og stop giver dig mulighed for at sætte alarmen på pause
  og genoptage lange alarmer.

Klik på OK, og en meddelelse vil informere dig om den aktuelt valgte
alarmvarighed.

[1]: https://addons.nvda-project.org/files/get.php?file=cac
[2]: https://www.nvaccess.org/addonStore/legacy?file=clock
