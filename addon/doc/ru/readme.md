# Clock and calendar Add-on for NVDA #

* Authors: Hrvoje Katić, Abdel and NVDA contributors
* Download [stable version][1]
* Download [development version][2]
* NVDA compatibility: 2019.3 and later

This add-on enables the advanced clock, alarm timer and calendar functionality for NVDA.

You can configure NVDA to announce time and date in formats other than what Windows provides by default. Additionally, you can obtain the current day, week number, as well as the remaining days before the end of the current year, and you can also set automatic time announcement on specified interval. There's also a stopwatch and Alarm timer features built-in to the add-on that lets you time your tasks, such as copying files, installing programs, or cooking meals.

Notes:

* if you install the add-on as an update, during the installation process, the wizard detects if the old configuration is compatible with the new one and offers to correct it before installing, then you'll just have to validate the OK button to confirm that.
* On Windows 10 and later, you can use Alarms and Clock app to manage stopwatch and timers.

## Key commands

* NVDA+F12: get current time
* NVDA+F12 pressed twice quickly: get current date
* NVDA+F12 pressed three times quickly: reports the current day, the week number, the current year and the remaining days before the end of the year
* NVDA+Shift+F12: enter clock layer

## Unassigned commands

The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands. To do so, open NVDA menu, Preferences, then Input Gestures. Expand Clock category, then locate unassigned commands from the list below and select "Add", then enter the gesture you wish to use.

* Elapsed and remaining time before the next alarm. pressing this gesture twice quickly will cancel the next alarm.
* Stop currently playing alarm sound.
* Display schedule alarms dialog box.
* Show layered commands (keys to be pressed after NVDA+Shift+F12).

## Layered commands

To use layered commands, press NVDA+Shift+F12 followed by one of the following keys:

* S: Starts, resets or stops the stopwatch
* R: Resets stopwatch to 0 without restarting it
* A: gives the elapsed and remaining time before the next alarm
* T: opens schedule alarms dialog.
* C: Cancel the next alarm
* Space: Speaks current stopwatch or count-down timer
* p: If an alarm is too long, allows to stop it
* H: List all layered commands (Help)

## Configuration and usage

To configure clock functionality, open NVDA menu, Preferences, then Settings, and configure the following options from Clock panel:

* Time and date display format: use these combo boxes to configure how NVDA will announce time and date when you press NVDA+F12 once or twice quickly, respectively.
* Interval: choose the time announcement interval from this combo box (off, every 10 minutes, 15 minutes, 30 minutes, or every hour).
* Time announcement (enabled if interval is not off): choose between speech and sound, sound only, or speech only.
* Clock chime sound (enabled if interval is not off): Select the default clock chime sound for  intermediate minutes and the top of the hour.
* Separate hour and intermediate minute chimes (enabled if interval is not off, disabled by default): Enable this checkbox to customize chimes for intermediate minutes separately from the hourly chime.
  * Intermediate minutes chime sound (enabled if "Separate hour and intermediate minute chimes" is checked): Select the clock chime sound specifically for intermediate minutes.
* Quiet hours (enabled if interval is not off): select this checkbox to configure quiet hours range when automatic time announcement should not occur.
* Quiet hours time format (enabled if quiet hours is enabled): select how quiet hours options are presented (12-hour or 24-hour format).
* Quiet hours start and end times: select hour and minute range for quiet hours from hours and minutes combo boxes.

To schedule alarms, open NVDA menu, Tools, then select Schedule Alarms. The dialog contents include:

* Alarm duration in: select alarm/timer duration between hours, minutes, and seconds.
* Duration: enter alarm duration in the unit specified above.
* Alarm sound: select the alarm sound to be played.
* Stop and pause buttons: stop or pause a long alarm sound.

Click OK, and a message will inform you the curretnly selected alarm duration.

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
