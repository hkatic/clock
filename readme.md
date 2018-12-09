# Clock and calendar Add-on for NVDA #

* Authors: Hrvoje Katić, Abdel and NVDA contributors;
* Download [stable version][1];
* Download [development version][2].


This addon enables the advanced clock, alarm timer and calendar functionality for NVDA. Instead of always getting time and date from Windows, you can customize how times and dates should be spoken and brailled by NVDA. Additionally, you can obtain the current day and week number of the current year, and you can also set automatic time announcement on specified interval. There's also a stopwatch and Alarm timer features built-in to the addon, that lets you time your tasks, such as copying files, installing programs, or cooking meals.

## Usage

*	Open the configuration dialog for this addon from the NVDA tools menu or from the settings panel According to your version of NVDA;
	*	In the Clock setup dialog, the first two Combo Box controls allow you to choose your prefered time and date display formats;
	*	The Checkbox control labeled "input in 24-hour format" allows you to configure wether you want to input time for quiet hours in 12-hour (A.M. or P.M.), or european 24-hour format;
	*	The Combo Box control labeled "Auto-announce interval" allows you to set the interval for automatic time announcement (Every 15 minutes, Every 30 minutes, Every hour, or Off);
	*	The Combo Box control labeled "Time announcement" lets you configure how the automatic time announcement should be reported (Speech and sound, Speech only, or Sound only) when automatic time announcement is working;
	*	The Combo box control labeled "Clock chime sound" lets you choose between various clock sounds that will be played when automatic time announcement is working and reported with sound;
	*	The Checkbox control labeled "Quiet hours" lets you configure time range when automatic time announcement shouldn't occure, no matter if automatic time announcement is enabled or not;
	*	The Edit box controls for start and end time (only visible if quiet hours are enabled) let you configure time range for quiet hours. The time should be entered in HH:MM format;
	*	When done, tab to the OK button and activate it by pressing Enter to save your settings;
	*	In the Alarm setup dialog, the first Combo Box control allow you to choose your prefered countdown timer before the alarm ring;
	*	The Edit box control lets you type your time waiting before the alarm ring. This duration must be specified in 1 or more digits, not a decimal number;
	*	The Combo box control labeled "Alarm sound" lets you choose between various alarm sounds that will be played when the alarm time arrives;
	*	When done, tab to the OK button and activate it by pressing Enter. A message should be displayed to remind you of the waiting time before the alarm;
*	Press NVDA+F12 once to get current time, twice to get current date, or thrice to get the current day and week number of the current year.

## Key commands

- NVDA+F12, get current time;
- NVDA+F12 pressed twice quickly, get current date;
- NVDA+F12 pressed thrice quickly, reports the current day, the week number, the current year and the days remaining before the end of the year.

- Control+F12, gives the remaining and elapsed time before the next alarm;
- Control+F12 pressed twice quickly, cancel the next alarm.

## Layered commands

To use layered commands, press NVDA+Shift+F12 followed by one of the following keys:

- S: Starts, resets or stops the stopwatch;
- R: Resets stopwatch to 0 without restarting it;
- A: gives the remaining and elapsed time before the next alarm;
- C: Cancel the next alarm;
- Spacebar: Speaks current stopwatch or count-down timer;
- H: List all layered commands (Help).

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
