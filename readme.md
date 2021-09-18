# Clock and calendar Add-on for NVDA #

* Authors: Hrvoje Katić, Abdel and NVDA contributors
* Download [stable version][1]
* Download [development version][2]
* NVDA compatibility: 2019.3 and beyond

This add-on enables the advanced clock, alarm timer and calendar functionality for NVDA.

You can configure NvDA to announce time and date in formats other than what Windows provides by default. Additionally, you can obtain the current day, week number, as well as the remaining days before the end of the current year, and you can also set automatic time announcement on specified interval. There's also a stopwatch and Alarm timer features built-in to the add-on that lets you time your tasks, such as copying files, installing programs, or cooking meals.

Notes:

* if you install the add-on as an update, during the installation process, the wizard detects if the old configuration is compatible with the new one and offers to correct it before installing, then you'll just have to validate the OK button to confirm that.
* On Windows 10 and later, you can use Alarms and Clock app to manage stopwatch and timers.

## Key commands

* NVDA+F12: get current time
* NVDA+F12 pressed twice quickly: get current date
* NVDA+F12 pressed three times quickly: reports the current day, the week number, the current year and the remaining days before the end of the year
* NVDA+Shift+F12: enter clock layer

## Unassigned commands

The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands. To do so, open NVDA menu, Preferences, then Input Gestures. Expand Clock category, then locate unassigned commands from the list below and select "Add", then type the gesture you wish to use.

* Elapsed and remaining time before the next alarm. pressing this gesture twice quickly will cancel the next alarm.
* Stop currently playing alarm sound.

## Layered commands

To use layered commands, press NVDA+Shift+F12 followed by one of the following keys:

* S: Starts, resets or stops the stopwatch
* R: Resets stopwatch to 0 without restarting it
* A: gives the elapsed and remaining time before the next alarm
* C: Cancel the next alarm
* Space: Speaks current stopwatch or count-down timer
* p: If an alarm is too long, allows to stop it
* H: List all layered commands (Help)

## Usage

*	Open the configuration dialog for this add-on from NVDA Settings dialog.
	*	In the Clock setup panel, the first two Combo Box controls allow you to choose your prefered time and date display formats.
	*	The Combo Box control labeled "Interval" allows you to set the interval for automatic time announcement (Every 10 minutes, Every 15 minutes, Every 30 minutes, Every hour, or Off).
	*	The Combo Box control labeled "Time announcement" (only visible if the choice "off" is not selected in the interval Combo Box) lets you configure how the automatic time announcement should be reported (Speech and sound, Speech only, or Sound only) when automatic time announcement is working.
	*	The Combo box control labeled "Clock chime sound" (only visible if the choice "off" is not selected in the interval Combo Box) lets you choose between various clock sounds that will be played when automatic time announcement is working and reported with sound.
	*	The Checkbox control labeled "Quiet hours" (only visible if the choice "off" is not selected in the interval Combo Box) lets you configure time range when automatic time announcement shouldn't occur.
	*	The Checkbox control labeled "input in 24-hour format" (only visible if quiet hours are enabled) allows you to configure whether you want to input time for quiet hours in 12-hour (A.M. or P.M.), or european 24-hour format.
	*	The Edit box controls for start and end time (only visible if quiet hours are enabled) let you configure time range for quiet hours. The time should be entered in HH:MM format if the "input in 24-hour format" checkbox is checked, otherwise you must use a 12 hour format as described below.
	*	When done, tab to the OK button and activate it by pressing Enter to save your settings.
	*	In the Alarm setup dialog, the first Combo Box control allow you to choose your prefered countdown timer before the alarm ring.
	*	The Edit box control lets you type your time waiting before the alarm ring. This duration must be specified in 1 or more digits, not a decimal number.
	*	The Combo box control labeled "Alarm sound" lets you choose between various alarm sounds that will be played when the alarm time arrives.
	*	The pause button allows you to pause/resume too long alarms.
	*	The stop button allows you to stop too long alarms.
	*	When done, tab to the OK button and activate it by pressing Enter. A message should be displayed to remind you of the waiting time before the alarm.
*	Press NVDA+F12 once to get current time, twice to get current date, or three times to get the current day, week number, as well as the remaining days before the end of the current year.

## Syntax to use for quiet hours

1. To avoid bugs, the quiet hours must follow a rigorous and precise syntax.
2. If you check the "Input in 24-hour format" checkbox, the format must be "HH:MM".
3. If you uncheck the "Input in 24-hour format" checkbox, the format must be "HH:MM AM" or "HH:MM PM", the HH must contain a 12-hour format, from 0 to 12 and the "AM"|"PM" suffix can be in lowercase or uppercase.
4. If you check the Quiet hours" checkbox and keep the "Quiet hours start time" or "Quiet hours end time" field empty, or type a mistaken value, the "Quiet hours" checkbox will be unchecked automatically to avoid errorss and a message will be displayed.

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
