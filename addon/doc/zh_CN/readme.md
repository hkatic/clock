# NVDA 时钟和日历插件

- 作者：Hrvoje Katić, Abdel and NVDA contributors
- 下载 [稳定版][1]
- 下载 [开发版][2]
- NVDA 兼容性：2019.3 及更高版本

此插件为 NVDA 启用了高级时钟、闹钟和日历功能。

You can configure NVDA to announce time and date in formats other than what Windows provides by default. Additionally, you can obtain the current day, week number, as well as the remaining days before the end of the current year, and you can also set automatic time announcement on specified interval. There's also a stopwatch and Alarm timer features built-in to the add-on that lets you time your tasks, such as copying files, installing programs, or cooking meals.

注：

- 如果您正在安装的插件高于先前版本，在安装过程中，安装向导会检测旧配置是否与新配置兼容，并可以进行相应的自动更正，在此过程中您只需确认即可。
- 在 Windows 10 及以后版本的操作系统上，您可以使用闹钟和提醒应用程序来管理秒表和计时器。

## 键盘命令

- NVDA+F12：读出当前时间
- NVDA+F12 连按两次：读出当前日期
- NVDA+F12 连按三次：读出当前日期，周数、年份及本年的剩余天数
- NVDA+Shift+F12：打开时钟命令面板

## 未分配的命令

The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands. To do so, open NVDA menu, Preferences, then Input Gestures. Expand Clock category, then locate unassigned commands from the list below and select "Add", then enter the gesture you wish to use.

- Elapsed and remaining time before the next alarm. pressing this gesture twice quickly will cancel the next alarm.
- 停止当前响铃。
- 显示提醒设置对话框。
- 显示命令面板（在按 NVDA+Shift+F12 后需要按下的按键）。

## 命令面板

要使用命令面板，请先按NVDA + Shift + F12，然后按下相应功能的对应快捷键：

- s : 启动、重置或停止秒表
- r : 重置秒表但不重新开始
- A: 读出距离下依次提醒的已经过时间和剩余时间
- t: 显示提醒设置对话框。
- c : 取消下一个提醒
- 空格 : 读出当前秒表或上次计时器的时间
- p : 停止响铃（如果响铃时间过长）
- H: List all layered commands (Help)

## 设置和使用

要设置时钟插件的功能，请打开 NvDA 菜单、选项、设置，然后在时钟面板设置以下选项：

- 时间和日期显示格式：使用这两个组合框来设置当您分别快速按 NVDA+F12 一次或两次时 NVDA 应该如何读出时间和日期。
- 报时间隔：在此组合框中选择报时间隔（关闭、每 10 分钟、15 分钟、30 分钟或每小时）。
- 报时方式（如果报时间隔未关闭则该设置有效）：在语音和音效、只有音效或只有语音之间进行选择。
- Clock chime sound (enabled if interval is not off): Select the default clock chime sound for  intermediate minutes and the top of the hour.
- Separate hour and intermediate minute chimes (enabled if interval is not off, disabled by default): Enable this checkbox to customize chimes for intermediate minutes separately from the hourly chime.
  - Intermediate minutes chime sound (enabled if "Separate hour and intermediate minute chimes" is checked): Select the clock chime sound specifically for intermediate minutes.
- 免打扰时段（仅在“报时间隔”组合框中未选择“关闭”选项时才可见）允许您设置不自动报时的时间范围。
- 免打扰时段时间格式：选择免打扰时段的显示方式（12 小时制或 24 小时制）。
- 免打扰时段的开始和结束时间：从小时和分钟组合框中选择免打扰时段的开始和结束时间点。

要设置提醒，请打开 NVDA 菜单,工具,设置提醒，设置对话框内包括： The dialog contents include:

- Alarm duration in: select alarm/timer duration between hours, minutes, and seconds.
- Duration: enter alarm duration in the unit specified above.
- 铃声：选择提醒时播放的铃声。
- 停止和暂停按钮：停止或暂停较长的铃声预览。

Click OK, and a message will inform you the curretnly selected alarm duration.

[1]: https://addons.nvda-project.org/files/get.php?file=cac
[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
