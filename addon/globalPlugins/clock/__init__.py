# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

from typing import Tuple, Callable
import sys
import speech
from . import skipTranslation
import globalVars
from . import alarmHandler
import globalPluginHandler
import gui
from . import paths
import scriptHandler
from logHandler import log
import ui
from . import formats
from collections import Counter
import nvwave
from . import clockHandler
from . import stopwatchHandler
from .clockSettingsGUI import ClockSettingsPanel, AlarmSettingsDialog
import config
import tones
from datetime import datetime
import wx
import globalCommands
import os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__))))
from . import convertdate
sys.path.remove(sys.path[-1])
import time
from winKernel import GetTimeFormatEx, GetDateFormatEx
from configobj.validate import VdtTypeError

import addonHandler
addonHandler.initTranslation()
_: Callable[[str], str]

confspec = {
	'timeDisplayFormat': 'integer(default=0)',
	'dateDisplayFormat': 'integer(default=1)',
	'input24HourFormat': 'boolean(default=False)',
	'autoAnnounce': 'integer(default=0)',
	'timeReporting': 'integer(default=0)',
	'timeIntermediateReportSound': 'string(default="clock_chime1.wav")',
	'separateReportSounds': 'boolean(default=False)',
	'timeReportSound': 'string(default="clock_chime1.wav")',
	'alarmSound': 'string(default="alarm1.wav")',
	'alarmTimerChoice': 'integer(default=1)',
	'quietHours': 'boolean(default=False)',
	'alarmTime': 'float(default=0.0)',
	'alarmSavedTime': 'float(default=0.0)',
	'quietHoursStartTime': 'string(default="")',
	'quietHoursEndTime': 'string(default="")',
}
config.conf.spec["clockAndCalendar"] = confspec


def secondsToString(seconds: float) -> str:
	"""
	A function to convert seconds to user-friendly string, used for stopwatch and timer.
	@param second: The number of seconds to convert.
	@type seconds: float.
	@returns: User-friendly string containing hours, minutes and seconds.
	@rtype: basestring.
	"""
	text = ""
	seconds = int(seconds)
	min, sec = divmod(seconds, 60)
	hr, min = divmod(min, 60)
	if hr > 0:
		text += _("{hours} hours, ").format(hours=hr)
	if min > 0:
		text += _("{minutes} minutes, ").format(minutes=min)
	if sec > 0:
		text += _("{seconds} seconds").format(seconds=sec)
	return _("0 seconds") if not text else text


def getDayAndWeekOfYear(date: str) -> Tuple[int, ...]:
	"""
	A function to calculate the current day of the year, as well as the actual number of weeks,
	for a Gregorian year and also some non-Gregorian years.
	@param date: The current date that will allow to make the calculation.
	@type date: basestring.
	@returns: The day of year, the week number, the current year
	and the days remaining before the end of the current year.
	@rtype: tuple.
	"""
	now = datetime.now()
	# Convert date into a datetime object by parsing it.
	curDate = datetime.strptime(date, "%Y/%m/%d")
	curYear = curDate.year
	gregYear = now.year
	curMonth = curDate.month
	gregMonth = now.month
	curDay = curDate.day
	gregDay = now.day
	# Tuple components, remainig days will be obtained later.
	nDayOfYear = 0
	nWeekOfYear = 0
	nDaysForYear = 0
	if curYear == gregYear:
		# It's a Gregorian year.
		nDayOfYear = now.timetuple()[7]
		nWeekOfYear = now.isocalendar()[1]
		# Calculate the remaining days before the end of the current year.
		nDaysForYear = convertdate.gregorian.YEAR_DAYS
		if convertdate.gregorian.isleap(gregYear):
			nDaysForYear += 1
	else:
		# It's not a Gregorian year.
		dt1 = convertdate.islamic
		dt2 = convertdate.persian
		if (
			curYear == dt1.from_gregorian(gregYear, gregMonth, gregDay)[0]
			or curYear == dt2.from_gregorian(gregYear, gregMonth, gregDay)[0]
		):
			# It's a Hijri year.
			islamicYear = curYear == dt1.from_gregorian(gregYear, gregMonth, gregDay)[0]
			dt = dt1 if islamicYear else dt2
			# The number of weeks must take into account the day of the week
			# corresponding to the first day of the year.
			ndw = 6 if islamicYear else 5
			# Store month lengthhs which can be summed up to obtain number of days for a year.
			monthLengths = [dt.month_length(curYear, month) for month in range(1, 13)]
			# 0-based indexing means first month is index 0.
			# But since previous months have already passed, obtain sum of total days prior to this month.
			# For the first month, number of days is the same as current date.
			nDayOfYear = curDay
			if curMonth > 1:
				nDayOfYear += sum(monthLengths[:curMonth - 1])
			# Calculation of the weeks number.
			if nDayOfYear % 7 == 0:
				if dt.to_jd(curYear, 1, 1) == ndw:
					# The first day of the year corresponds to the first day of the week for the current Hidjri calendar.
					nWeekOfYear = nDayOfYear // 7
				else:
					# The first day of the year doesn't correspond to the
					# first day of the week for the current Hidjri calendar.
					nWeekOfYear = (nDayOfYear // 7) - 1
			else:
				if dt.to_jd(curYear, 1, 1) == ndw:
					# The first day of the year corresponds to the first day of the week for the current Hidjri calendar.
					nWeekOfYear = (nDayOfYear // 7) + 1
				else:
					# The first day of the year doesn't correspond
					# to the first day of the week for the current Hidjri calendar.
					nWeekOfYear = nDayOfYear // 7
			# Calculate the remaining days before the end of the current year.
			nDaysForYear = sum(monthLengths)
	daysRemaining = nDaysForYear - nDayOfYear
	if nWeekOfYear == 1 and nDayOfYear > 300:
		curYear += 1
	return (nDayOfYear, nWeekOfYear, curYear, daysRemaining)


def checkLocalTimeFormats():
	"""A function that checks that each localized time format is unique.
	In case two or more identical time formats are found, a warning is logged, to give translators the
	opportunity to improve their translations by translating uniquely each time format.
	"""
	fmtCounter = Counter(formats.timeFormats)
	for fmt, nbOccurrences in fmtCounter.items():
		if nbOccurrences > 1:
			log.debugWarning(f"The format '{fmt}' appears {nbOccurrences} times for the current localization.")


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translators: Script category for Clock addon commands in input gestures dialog.
	scriptCategory = _("Clock")
	clockLayerModeActive = False
	layeredScriptToRun = None

	def __init__(self):
		super().__init__()
		if globalVars.appArgs.secure or config.isAppX:
			return
		checkLocalTimeFormats()
		gui.NVDASettingsDialog.categoryClasses.append(ClockSettingsPanel)
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu
		self.alarmSettings = self.toolsMenu.Append(
			# Translators: The name of the alarm item in NVDA Tools menu.
			wx.ID_ANY, _("Schedule a&larms..."),
			# Translators: The tooltyp text for the alarm item in NVDA Tools menu.
			_("Allows you to schedule an alarm")
		)
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onAlarmSettingsDialog, self.alarmSettings)
		self.clock = clockHandler.Clock()
		self.stopwatch = stopwatchHandler.Stopwatch()
		conf = config.conf['clockAndCalendar']
		validationFailed = False
		try:
			conf['alarmTime']
		except VdtTypeError:
			validationFailed = True
			conf.profiles[0]['alarmTime'] = 0.0
		try:
			conf['timeDisplayFormat']
		except VdtTypeError:
			validationFailed = True
			conf.profiles[0]['timeDisplayFormat'] = 0
		try:
			conf['dateDisplayFormat']
		except VdtTypeError:
			conf.profiles[0]['dateDisplayFormat'] = 1
			validationFailed = True
		# We save the configuration, in case the user would not have checked the
		# "Save configuration on exit" checkbox in General settings.
		# Only do this if validation fails.
		if validationFailed and not config.conf['general']['saveConfigurationOnExit']:
			config.conf.save()
		if not config.conf['clockAndCalendar']['alarmSound'] in paths.LIST_ALARMS:
			alarmSound = paths.LIST_ALARMS[0]
		else:
			alarmSound = config.conf['clockAndCalendar']['alarmSound']
		if config.conf['clockAndCalendar']['alarmSavedTime'] != 0.0:
			wakeUp = config.conf['clockAndCalendar']['alarmTime'] - (
				time.time() - config.conf['clockAndCalendar']['alarmSavedTime']
			)
			alarmHandler.run = alarmHandler.AlarmTimer(
				wakeUp, alarmHandler.runAlarm, [os.path.join(paths.ALARMS_DIR, alarmSound)]
			)
			alarmHandler.run.start()
		# Clock layer gestures.
		self._clockLayerGestures = (
			("s", self.script_stopwatchRun),
			("r", self.script_stopwatchReset),
			("a", self.script_alarmInfo),
			("t", self.script_activateAlarmSettingsDialog),
			("c", self.script_cancelAlarm),
			("space", self.script_timeDisplay),
			("p", self.script_stopLongAlarm),
			("h", self.script_getHelp)
		)

	def terminate(self):
		super().terminate()
		gui.NVDASettingsDialog.categoryClasses.remove(ClockSettingsPanel)
		try:
			self.toolsMenu.Remove(self.alarmSettings)
		except (RuntimeError, AttributeError):
			pass
		self.clock.terminate()

	@scriptHandler.script(
		description=_(
			# Translators: Message presented in input help mode.
			"Speaks current time. If pressed twice quickly, speaks current date. "
			"If pressed three times quickly, reports the current day, the week number, "
			"the current year and the days remaining before the end of the year."
		),
		category=globalCommands.SCRCAT_SYSTEM,
		gesture="kb:NVDA+f12",
	)
	def script_reportTimeAndDate(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		now = datetime.now()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			msg = GetTimeFormatEx(
				None, None, now, formats.rgx.sub(
					formats.repl, formats.timeFormats[config.conf['clockAndCalendar']['timeDisplayFormat']]
				)
			)
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			msg = GetDateFormatEx(
				None, None, None, formats.dateFormats[config.conf['clockAndCalendar']['dateDisplayFormat']]
			)
		else:
			informations = getDayAndWeekOfYear(GetDateFormatEx(None, None, None, "yyyy/M/d"))
			msg = _(
				"Day {day}, week {week} of {year}, remaining days {remain}."
			).format(day=informations[0], week=informations[1], year=informations[2], remain=informations[3])
		ui.message(msg)
		speech.setSpeechMode(curMode)
	# We remove the docstring from the original dateTime script
	# to have only one entry in the "System status" category,
	# it will be automatically restored if the Clock add-on is disabled or uninstalled.
	globalCommands.commands.script_dateTime.__func__.__doc__ = ""

	def getScript(self, gesture):
		if not self.clockLayerModeActive:
			return super().getScript(gesture)
		script = super().getScript(gesture)
		if not script:
			return self.script_error
		self.layeredScriptToRun = next(
			(x[1] for x in self._clockLayerGestures if x[0] == gesture.mainKeyName), None
		)
		return self.runAndFinish

	def runAndFinish(self, gesture):
		if self.layeredScriptToRun is not None:
			self.layeredScriptToRun(gesture)
		else:
			ui.message("Can't find this layered script")
		# We call the finish method in all cases.
		self.finish()

	def finish(self):
		self.clockLayerModeActive = False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_error(self, gesture):
		tones.beep(120, 100)
		self.finish()

	@scriptHandler.script(
		description=_(
			# Translators: Message presented in input help mode.
			"Clock and calendar layer commands. After pressing this keystroke, press H for additional help."
		),
		gesture="kb:NVDA+shift+f12",
	)
	def script_clockLayerCommands(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		if self.clockLayerModeActive:
			self.script_error(gesture)
			return
		for gesture in self._clockLayerGestures:
			self.bindGesture("kb:%s" % gesture[0], gesture[1].__name__[7:])
		self.clockLayerModeActive = True
		tones.beep(100, 10)
		speech.setSpeechMode(curMode)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Starts, resets or stops the stopwatch."),
	)
	def script_stopwatchRun(self, gesture):
		curMode = speech.getState().speechMode
		if curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		if not self.stopwatch.running and self.stopwatch.startTime:
			self.stopwatch.reset()
			self.stopwatch.start()
			ui.message(_("Reset. Running."))
		elif not self.stopwatch.running:
			self.stopwatch.start()
			ui.message(_("Running."))
		else:
			self.stopwatch.stop()
			ui.message(_("{0} stopped.").format(secondsToString(self.stopwatch.elapsedTime())))
			speech.setSpeechMode(curMode)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Speaks current stopwatch or count-down timer."),
	)
	def script_timeDisplay(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		ui.message(secondsToString(self.stopwatch.elapsedTime()))
		speech.setSpeechMode(curMode)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Gives the remaining and elapsed time before the next alarm."),
	)
	def script_alarmInfo(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		if alarmHandler.run and alarmHandler.run.is_alive():
			elapsedTime = alarmHandler.run.elapsed()
			remainingTime = alarmHandler.run.remaining()
			msg = _(
				"Elapsed time {elapsed}, remaining time {remaining}."
			).format(elapsed=secondsToString(elapsedTime), remaining=secondsToString(remainingTime))
		else:
			msg = _("No alarm")
		ui.message(msg)
		speech.setSpeechMode(curMode)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Cancel the next alarm."),
	)
	def script_cancelAlarm(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		if alarmHandler.run and alarmHandler.run.is_alive():
			alarmHandler.run.cancel()
			msg = _("Alarm cancelled")
		else:
			msg = _("No alarm")
		ui.message(msg)
		speech.setSpeechMode(curMode)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Resets stopwatch to 0 without restarting it.")
	)
	def script_stopwatchReset(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		if self.stopwatch.startTime is None and self.stopwatch.stopTime is None and not self.stopwatch.running:
			ui.message(
				_("The stopwatch is already reset to 0. Use the clock layer command followed by s to start it.")
			)
			return
		self.stopwatch.reset()
		ui.message(_("Stopwatch reset."))
		speech.setSpeechMode(curMode)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Lists available commands in clock command layer."),
	)
	def script_getHelp(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		ui.message("\n".join(x[0] + " : " + x[1].__doc__ if x[0] != "space" else skipTranslation.translate(x[0]) + " : " + x[1].__doc__ for x in self._clockLayerGestures))  # NOQA: E501
		speech.setSpeechMode(curMode)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Lists available commands in clock command layer, showing them in browse mode."),
	)
	def script_getHelpInBrowseMode(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		browseableMessageText = "<ul><li>" + ("</li><li>".join(x[0] + " : " + x[1].__doc__ if x[0] != "space" else skipTranslation.translate(x[0]) + " : " + x[1].__doc__ for x in self._clockLayerGestures)) + "</li></ul>"  # NOQA: E501
		ui.browseableMessage(browseableMessageText, self.scriptCategory, isHtml=True)
		speech.setSpeechMode(curMode)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Allows to check the next alarm. If pressed twice, cancels it."),
	)
	def script_checkOrCancelAlarm(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		if alarmHandler.run and alarmHandler.run.is_alive():
			elapsedTime = alarmHandler.run.elapsed()
			remainingTime = alarmHandler.run.remaining()
			if scriptHandler.getLastScriptRepeatCount() > 0:
				alarmHandler.run.cancel()
				msg = _("Alarm cancelled")
			else:
				msg = _(
					"Elapsed time {elapsed}, remaining time {remaining}."
				).format(elapsed=secondsToString(elapsedTime), remaining=secondsToString(remainingTime))
		else:
			msg = _("No alarm")
		ui.message(msg)
		speech.setSpeechMode(curMode)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("If an alarm is too long, allows to stop it."),
	)
	def script_stopLongAlarm(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		msg = _("No sound is launched.")
		if nvwave.fileWavePlayer is not None:
			nvwave.fileWavePlayer.stop()
			msg = _("Sound stopped")
		ui.message(msg)
		speech.setSpeechMode(curMode)

	def onAlarmSettingsDialog(self, evt):
		try:
			gui.mainFrame.prePopup()
			d = AlarmSettingsDialog(gui.mainFrame)
			d.Show()
			gui.mainFrame.postPopup()
		except gui.settingsDialogs.SettingsDialog.MultiInstanceErrorWithDialog:
			wx.CallAfter(
				gui.messageBox,
				# Translators: error message when attempting to open more than one alarm settings dialogs.
				_("Schedule alarms dialog is already open."),
				skipTranslation.translate("Error"), wx.OK | wx.ICON_ERROR
			)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Display the clock settings dialog box."),
	)
	def script_activateClockSettingsDialog(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		wx.CallAfter(gui.mainFrame._popupSettingsDialog, gui.NVDASettingsDialog, ClockSettingsPanel)
		speech.setSpeechMode(curMode)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Display schedule alarms dialog box."),
	)
	def script_activateAlarmSettingsDialog(self, gesture):
		curMode = speech.getState().speechMode
		if hasattr(speech.SpeechMode, "onDemand") and curMode == speech.SpeechMode.onDemand:
			speech.setSpeechMode(speech.SpeechMode.talk)
		wx.CallAfter(self.onAlarmSettingsDialog, None)
		speech.setSpeechMode(curMode)
