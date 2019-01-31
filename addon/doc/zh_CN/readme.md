# NVDA 时钟日历插件 #

* 作者: Hrvoje Katić, Abdel and NVDA contributors;
* 下载 [稳定版][1]
* 下载 [开发板][2]


此插件可为NVDA启用高级时钟，闹钟定时器和日历功能。

您可以自定义NVDA应如何读出时间和日期，而不是从Windows获取时间日期。

此外，您还可以获取当前日期，周数以及当前年度结束前的剩余天数，还可以按指定的时间间隔设置自动时间通知。

还有内置于插件的秒表和闹钟定时器功能，可让您为任务计时，例如复制文件，安装程序或烹饪。

## 注意:

如果您将插件安装为更新，则在安装过程中，向导会检测旧配置是否与新配置兼容，并在安装之前提供更正，然后您只需确定即可。

## 使用

*	Open the configuration dialog for this addon from the NVDA tools menu or from the settings panel According to your version of NVDA;
	*	In the Clock setup dialog, the first two Combo Box controls allow you to choose your prefered time and date display formats;
	*	The Combo Box control labeled "Interval" allows you to set the interval for automatic time announcement (Every 10 minutes, Every 15 minutes, Every 30 minutes, Every hour, or Off);
	*	The Combo Box control labeled "Time announcement" (only visible if the choice "off" is not selected in the interval Combo Box) lets you configure how the automatic time announcement should be reported (Speech and sound, Speech only, or Sound only) when automatic time announcement is working;
	*	The Combo box control labeled "Clock chime sound" (only visible if the choice "off" is not selected in the interval Combo Box) lets you choose between various clock sounds that will be played when automatic time announcement is working and reported with sound;
	*	The Checkbox control labeled "Quiet hours" (only visible if the choice "off" is not selected in the interval Combo Box) lets you configure time range when automatic time announcement shouldn't occure;
	*	The Checkbox control labeled "input in 24-hour format" (only visible if quiet hours are enabled) allows you to configure wether you want to input time for quiet hours in 12-hour (A.M. or P.M.), or european 24-hour format;
	*	The Edit box controls for start and end time (only visible if quiet hours are enabled) let you configure time range for quiet hours. The time should be entered in HH:MM format if the "input in 24-hour format" checkbox is checked, otherwise you must use a 12 hour format as described below;
	*	When done, tab to the OK button and activate it by pressing Enter to save your settings;
	*	In the Alarm setup dialog, the first Combo Box control allow you to choose your prefered countdown timer before the alarm ring;
	*	The Edit box control lets you type your time waiting before the alarm ring. This duration must be specified in 1 or more digits, not a decimal number;
	*	The Combo box control labeled "Alarm sound" lets you choose between various alarm sounds that will be played when the alarm time arrives;
	*	The pause button allows you to pause/resume too long alarms;
	*	The stop button allows you to stop too long alarms;
	*	When done, tab to the OK button and activate it by pressing Enter. A message should be displayed to remind you of the waiting time before the alarm;
*	Press NVDA+F12 once to get current time, twice to get current date, or thrice to get the current day, week number, as well as the remaining days before the end of the current year.

## 键盘命令

NVDA + F12，读出当前时间。 NVDA + F12快速按两次，读出当前日期。 NVDA +
F12快速按三次，读出当天，周数，当前年份和今年年底前的剩余天数。

- There is a script that gives the remaining and elapsed time before the
next alarm; - There is no keyboard gesture assigned to this script, you will
have to do it yourself in the "Input gestures" dialog box, in the "Clock"
category; - This gesture pressed twice quickly, cancel the next alarm; -
There is another script to stop the sound that is currently playing, its
gesture is also not defined; - That script can also be called using the
clock layer commands described below.

## 分层命令

要使用分层命令，请按NVDA + Shift + F12，然后按以下快捷键:

- S: Starts, resets or stops the stopwatch; - R: Resets stopwatch to 0
without restarting it; - A: gives the remaining and elapsed time before the
next alarm; - C: Cancel the next alarm; - Space: Speaks current stopwatch or
count-down timer; - p: If an alarm is too long, allows to stop it; - H: List
all layered commands (Help).

## Syntax to use for quiet hours

- To avoid bugs, the quiet hours must follow a rigorous and precise syntax;
- If you check the "Input in 24-hour format" checkbox, the format must be
"HH:MM"; - If you uncheck the "Input in 24-hour format" checkbox, the format
must be "HH:MM AM" or "HH:MM PM", the HH must contain a 12-hour format, from
0 to 12 and the "AM"|"PM" suffix can be in lowercase or uppercase - If you
check the Quiet hours" checkbox and keep the "Quiet hours start time" or
"Quiet hours end time" field empty, or type a mistaken value, the "Quiet
hours" checkbox will be unchecked automatically, to avoid errors; - A
message should be displayed to report your error.

## 兼容性

- 此插件支持2014.3至2019.1的NVDA版本。


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

