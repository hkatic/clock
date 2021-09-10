# NVDA 时钟日历插件 #

* Authors: Hrvoje Katić, Abdel and NVDA contributors
* Download [stable version][1]
* Download [development version][2]
* NVDA compatibility: 2019.3 and beyond

This add-on enables the advanced clock, alarm timer and calendar
functionality for NVDA.

您可以自定义NVDA应如何读出时间和日期，而不是从Windows获取时间日期。

此外，您还可以获取当前日期，周数以及当前年度结束前的剩余天数，还可以按指定的时间间隔设置自动时间通知。

There's also a stopwatch and Alarm timer features built-in to the add-on
that lets you time your tasks, such as copying files, installing programs,
or cooking meals.

## 注意:

如果您将插件安装为更新，则在安装过程中，向导会检测旧配置是否与新配置兼容，并在安装之前提供更正，然后您只需确定即可。

## 使用

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

## 键盘命令

* NVDA+F12: get current time
* NVDA+F12 pressed twice quickly: get current date
* NVDA+F12 pressed three times quickly: reports the current day, the week
  number, the current year and the remaining days before the end of the
  year.
* There is a script that gives the remaining and elapsed time before the
  next alarm. There is no keyboard gesture assigned to this script, you will
  have to do it yourself in the "Input gestures" dialog box, in the "Clock"
  category. pressing this gesture twice quickly will cancel the next alarm.
* There is another script to stop the sound that is currently playing, its
  gesture is also not defined. That script can also be called using the
  clock layer commands described below.

## 分层命令

要使用分层命令，请按NVDA + Shift + F12，然后按以下快捷键:

* S: 启动，重置或停止秒表;
* R: 将秒表重置为0而不重新启动;
* A: 给出下一次闹钟前的剩余时间和经过时间;
* C: 取消下一个闹钟;
* Space: 读出当前的秒表或倒计时器;
* p: 如果闹钟太长，则允许停止闹钟;
* H: 列出所有分层命令（帮助）。

## 用于夜间模式的语法

* To avoid bugs, the quiet hours must follow a rigorous and precise syntax.
* If you check the "Input in 24-hour format" checkbox, the format must be
  "HH:MM".
* If you uncheck the "Input in 24-hour format" checkbox, the format must be
  "HH:MM AM" or "HH:MM PM", the HH must contain a 12-hour format, from 0 to
  12 and the "AM"|"PM" suffix can be in lowercase or uppercase.
* If you check the Quiet hours" checkbox and keep the "Quiet hours start
  time" or "Quiet hours end time" field empty, or type a mistaken value, the
  "Quiet hours" checkbox will be unchecked automatically to avoid errorss
  and a message will be displayed.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
