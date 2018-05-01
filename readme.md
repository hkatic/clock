# Clock and calendar Add-on for NVDA #

* Authors: Hrvoje Katić.
* Download [development version](https://github.com/hkatic/clock/releases/download/untagged-f0a8e8a85c97dce2ed7d/clock-1.0dev.nvda-addon)

This addon enables the advanced clock and calendar functionality for NVDA. Instead of always getting time and date from Windows, you can customize how times and dates should be spoken and brailled by NVDA. Additionally, you can obtain the current day and week number of the current year, and you can also set automatic time announcement on specified interval.

## Usage

*	Open the configuration dialog for this addon from the NVDA Preferences menu.
	*	The first two Combo Box controls allow you to choose your prefered time and date display formats.
	*	The Checkbox control labeled "input in 24-hour format" allows you to configure wether you want to input time for quiet hours in 12-hour (A.M. or P.M.), or european 24-hour format.
	*	The Combo Box control labeled "Auto-announce interval" allows you to set the interval for automatic time announcement (Every 15 minutes, Every 30 minutes, Every hour, or Off).
	*	The Combo Box control labeled "Time announcement" lets you configure how the automatic time announcement should be reported (Speech and sound, Speech only, or Sound only) when automatic time announcement is working.
	*	The Combo box control labeled "Clock chime sound" lets you choose between various clock sounds that will be played when automatic time announcement is working and reported with sound.
	*	The Checkbox control labeled "Quiet hours" lets you configure time range when automatic time announcement shouldn't occure, no matter if automatic time announcement is enabled or not.
	*	The Edit box controls for start and end time (only visible if quiet hours are enabled) let you configure time range for quiet hours.
	*	When done, tab to the OK button and activate it to save your settings.
*	Press NVDA+F12 once to get current time, twice to get current date, or thrice to get the current day and week number of the current year.

## Key commands

- NVDA+F12, get current time.
- NVDA+F12 pressed twice quickly, get current date.
- NVDA+F12 pressed thrice quickly, get the current day and week number of the current year.

## Layered commands

To use layered commands, press NVDA+Shift+F12 followed by one of the following keys:

- S: Starts, resets or stops the stopwatch.
- R: Resets stopwatch to 0 without restarting it.
- Spacebar: Speaks current stopwatch or count-down timer.
- H: List all layered commands (Help).


