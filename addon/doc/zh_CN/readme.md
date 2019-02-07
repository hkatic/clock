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

* Open the configuration dialog for this addon from the NVDA tools menu or
  from the settings panel According to your version of NVDA;

    * In the Clock setup dialog, the first two Combo Box controls allow you
      to choose your prefered time and date display formats;
    * The Combo Box control labeled "Interval" allows you to set the
      interval for automatic time announcement (Every 10 minutes, Every 15
      minutes, Every 30 minutes, Every hour, or Off);
    * The Combo Box control labeled "Time announcement" (only visible if the
      choice "off" is not selected in the interval Combo Box) lets you
      configure how the automatic time announcement should be reported
      (Speech and sound, Speech only, or Sound only) when automatic time
      announcement is working;
    * The Combo box control labeled "Clock chime sound" (only visible if the
      choice "off" is not selected in the interval Combo Box) lets you
      choose between various clock sounds that will be played when automatic
      time announcement is working and reported with sound;
    * The Checkbox control labeled "Quiet hours" (only visible if the choice
      "off" is not selected in the interval Combo Box) lets you configure
      time range when automatic time announcement shouldn't occure;
    * The Checkbox control labeled "input in 24-hour format" (only visible
      if quiet hours are enabled) allows you to configure wether you want to
      input time for quiet hours in 12-hour (A.M. or P.M.), or european
      24-hour format;
    * The Edit box controls for start and end time (only visible if quiet
      hours are enabled) let you configure time range for quiet hours. The
      time should be entered in HH:MM format if the "input in 24-hour
      format" checkbox is checked, otherwise you must use a 12 hour format
      as described below;
    * When done, tab to the OK button and activate it by pressing Enter to
      save your settings;
    * In the Alarm setup dialog, the first Combo Box control allow you to
      choose your prefered countdown timer before the alarm ring;
    * The Edit box control lets you type your time waiting before the alarm
      ring. This duration must be specified in 1 or more digits, not a
      decimal number;
    * The Combo box control labeled "Alarm sound" lets you choose between
      various alarm sounds that will be played when the alarm time arrives;
    * The pause button allows you to pause/resume too long alarms;
    * The stop button allows you to stop too long alarms;
    * When done, tab to the OK button and activate it by pressing Enter. A
      message should be displayed to remind you of the waiting time before
      the alarm;

* Press NVDA+F12 once to get current time, twice to get current date, or
  thrice to get the current day, week number, as well as the remaining days
  before the end of the current year.

## 键盘命令

* NVDA+F12,朗读当前时间;
* NVDA+F12 快速按两次，朗读当前日期;
* NVDA+F12 快速按三次，朗读当天，周数，当前年份和年底前的剩余天数。
* 有一个脚本可以在下一个闹钟之前提供剩余和经过时间;
* 没有为此脚本分配键盘手势，您必须在“输入手势”对话框的“时钟”类别中自行设置;
* 此手势快速按下两次，取消下一次闹钟;
* 另外还有另一个脚本可以停止当前播放的声音，其手势也没有定义;
* 也可以使用下面描述的时钟层命令调用该脚本。

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

* 为了避免错误，夜间模式必须遵循严格而精确的语法;
* 如果选中“24小时格式输入”复选框，则格式必须为“HH：MM”;
* 如果取消选中“以24小时格式输入”复选框，格式必须为“HH：MM AM”或“HH：MM PM”，HH必须包含12小时格式，从0到12和“AM”
  “|”PM“后缀可以是小写或大写
* 如果选中“夜间模式”复选框并保持“夜间模式开始时间”或“夜间模式结束时间”字段为空，或键入错误值，则会自动取消选中“夜间模式”复选框以避免错误;
* 应显示一条消息以朗读您的错误。

## 兼容性

* 此插件支持2014.3至2019.1的NVDA版本。


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

