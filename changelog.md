## Changes for 20260330.0.0

* Precision time announcement: when "Speech and sound" is selected, chime sounds now start playing *before* the minute boundary so they finish exactly on :00, followed immediately by speech announcing the live current time. Previously, the sound and speech both started at :00, causing the time to be announced several seconds late.
* BBC pips support (clock_cuckoo7.wav): the time signal's five short pips lead into a sixth long pip that lands precisely on the minute boundary, replicating the behaviour of a real broadcast time signal. Speech fires with the sixth pip.
* Sound-only mode: BBC pips retains its precision timing (sixth pip on :00); all other chime sounds play at :00 as before.
* Speech-only mode is unchanged.
* Added `safeGetTimeFormatEx` and `safeGetDateFormatEx` wrappers in formats.py for compatibility with NVDA 2024.2+ (ctypes no longer accepts None for DWORD arguments).
* Safe date format building at import time to prevent crashes from locale or API changes.

## Changes for 20260221.0.1

* Used the latest version of the addonTemplate.
