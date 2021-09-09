# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

import sys
from . import skipTranslation
import globalVars
from . import alarmHandler
import globalPluginHandler
import gui
from . import paths
import scriptHandler
import ui
from . import formats
import nvwave
from . import clockHandler
from . import stopwatchHandler
from .clockSettingsGUI import ClockSettingsPanel, AlarmSettingsPanel
import config
import tones
from datetime import datetime
import wx
import globalCommands
import os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__))))
from . import ephem
from . import pytz
from . import convertdate
sys.path.remove(sys.path[-1])
import time
from winKernel import GetTimeFormatEx, GetDateFormatEx
from configobj.validate import VdtTypeError

import addonHandler
addonHandler.initTranslation()


confspec = {
	'timeDisplayFormat': 'integer(default=0)',
	'dateDisplayFormat': 'integer(default=1)',
	'input24HourFormat': 'boolean(default=False)',
	'autoAnnounce': 'integer(default=0)',
	'timeReporting': 'integer(default=0)',
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


def secondsToString(seconds):
	"""
	A function to convert seconds to user-friendly string, used for stopwatch and timer.
	@param second: The number of seconds to convert.
	@type seconds: float.
	@returns: User-friendly string containing hours, minutes and seconds.
	@rtype: basestring.
	"""
	text = ""
	tm = time.gmtime(seconds)
	hr = tm.tm_hour
	if hr > 0:
		if hr > 23:
			hr = 24 * (hr / 24) + (hr % 24)
		text += _(u"{hours} hours, ").format(hours=str(hr))
	if tm.tm_min:
		text += _(u"{minutes} minutes, ").format(minutes=tm.tm_min)
	if tm.tm_sec:
		text += _(u"{seconds} seconds").format(seconds=tm.tm_sec)
	return _(u"0 seconds") if not text else text


def getDayAndWeekOfYear(date):
	"""
	A function to calculate the current day of the year, as well as the actual number of weeks, for a Gregorian year and also some non-Gregorian years.
	@param date: The current date that will allow to make the calculation.
	@type date: basestring.
	@returns: The day of year, the week number, the current year and the days remaining before the end of the current year.
	@rtype: tuple.
	"""
	now = datetime.now()
	curYear = int(date.split("/")[0])
	gregYear = int(now.strftime("%Y"))
	curMonth = int(date.split("/")[1])
	gregMonth = int(now.strftime("%m"))
	curDay = int(date.split("/")[2])
	gregDay = int(now.strftime("%d"))
	if curYear == gregYear:
		# It's a Gregorian year.
		nDayOfYear = now.timetuple()[7]
		nWeekOfYear = now.isocalendar()[1]
		if nWeekOfYear == 1 and nDayOfYear > 300:
			msg = [nDayOfYear, nWeekOfYear, gregYear + 1]
		else:
			msg = [nDayOfYear, nWeekOfYear, gregYear]
	else:
		# It's not a Gregorian year.
		dt1 = convertdate.islamic
		dt2 = convertdate.persian
		if curYear == dt1.from_gregorian(gregYear, gregMonth, gregDay)[0] or curYear == dt2.from_gregorian(gregYear, gregMonth, gregDay)[0]:
			# It's a Hijri year.
			dt = dt1 if curYear == dt1.from_gregorian(gregYear, gregMonth, gregDay)[0] else dt2
			# The number of weeks must take into account the day of the week corresponding to the first day of the year.
			ndw = 6 if curYear == dt1.from_gregorian(gregYear, gregMonth, gregDay)[0] else 5
			nDayOfYear = 0
			for month in range(1, curMonth):
				nDayOfYear += dt.month_length(curYear, month)
			nDayOfYear += curDay
			# Calculation of the weeks number.
			if nDayOfYear % 7 == 0:
				if dt.to_jd(curYear, 1, 1) == ndw:
					# The first day of the year corresponds to the first day of the week for the current Hidjri calendar.
					nWeekOfYear = nDayOfYear / 7
				else:
					# The first day of the year doesn't corresponds to the first day of the week for the current Hidjri calendar.
					nWeekOfYear = (nDayOfYear / 7) - 1
			else:
				if dt.to_jd(curYear, 1, 1) == ndw:
					# The first day of the year corresponds to the first day of the week for the current Hidjri calendar.
					nWeekOfYear = (nDayOfYear / 7) + 1
				else:
					# The first day of the year doesn't corresponds to the first day of the week for the current Hidjri calendar.
					nWeekOfYear = nDayOfYear / 7
			nWeekOfYear = int(nWeekOfYear)
			if nWeekOfYear == 1 and nDayOfYear > 300:
				msg = [nDayOfYear, nWeekOfYear, curYear + 1]
			else:
				msg = [nDayOfYear, nWeekOfYear, curYear]

	# Calculate the remaining days before the end of the current year.
	if curYear == gregYear:
		# It's a Gregorian year.
		total = convertdate.gregorian.YEAR_DAYS
		if convertdate.gregorian.isleap(gregYear):
			total += 1
		nDayOfYear = int(now.timetuple()[7])
	else:
		# It's a Hijri year.
		total = 0
		for month in range(1, 13):
			total += dt.month_length(curYear, month)
	daysRemaining = total - nDayOfYear
	msg.append(daysRemaining)
	return tuple(msg)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# Translators: Script category for Clock addon commands in input gestures dialog.
	scriptCategory = _("Clock")
	clockLayerModeActive = False
	layeredScriptToRun = None

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		if globalVars.appArgs.secure or config.isAppX:
			return
		gui.NVDASettingsDialog.categoryClasses.append(ClockSettingsPanel)
		gui.NVDASettingsDialog.categoryClasses.append(AlarmSettingsPanel)
		self.clock = clockHandler.Clock()
		self.stopwatch = stopwatchHandler.Stopwatch()
		try:
			config.conf['clockAndCalendar']['alarmTime']
		except VdtTypeError:
			conf = config.conf['clockAndCalendar']
			conf.profiles[0]['alarmTime'] = 0.0
			# We save the configuration, in case the user would not have checked the "Save configuration on exit" checkbox in General settings.
			if not config.conf['general']['saveConfigurationOnExit']:
				config.conf.save()
		try:
			config.conf['clockAndCalendar']['timeDisplayFormat']
		except VdtTypeError:
			conf = config.conf['clockAndCalendar']
			conf.profiles[0]['timeDisplayFormat'] = 0
			# We save the configuration, in case the user would not have checked the "Save configuration on exit" checkbox in General settings.
			if not config.conf['general']['saveConfigurationOnExit']:
				config.conf.save()
		try:
			config.conf['clockAndCalendar']['dateDisplayFormat']
		except VdtTypeError:
			conf = config.conf['clockAndCalendar']
			conf.profiles[0]['dateDisplayFormat'] = 1
			# We save the configuration, in case the user would not have checked the "Save configuration on exit" checkbox in General settings.
			if not config.conf['general']['saveConfigurationOnExit']:
				config.conf.save()
		if not config.conf['clockAndCalendar']['alarmSound'] in paths.LIST_ALARMS:
			alarmSound = paths.LIST_ALARMS[0]
		else:
			alarmSound = config.conf['clockAndCalendar']['alarmSound']
		if config.conf['clockAndCalendar']['alarmSavedTime'] != 0.0:
			wakeUp = config.conf['clockAndCalendar']['alarmTime'] - (time.time() - config.conf['clockAndCalendar']['alarmSavedTime'])
			alarmHandler.run = alarmHandler.AlarmTimer(wakeUp, alarmHandler.runAlarm, [os.path.join(paths.ALARMS_DIR, alarmSound)])
			alarmHandler.run.start()
		# Clock layer gestures.
		self._clockLayerGestures = (
			("s", self.script_stopwatchRun),
			("r", self.script_stopwatchReset),
			("a", self.script_alarmInfo),
			("c", self.script_cancelAlarm),
			("space", self.script_timeDisplay),
			("p", self.script_stopLongAlarm),
			("h", self.script_getHelp)
		)

	def terminate(self):
		super(GlobalPlugin, self).terminate()
		gui.NVDASettingsDialog.categoryClasses.remove(ClockSettingsPanel)
		gui.NVDASettingsDialog.categoryClasses.remove(AlarmSettingsPanel)
		self.clock.terminate()

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Speaks current time. If pressed twice quickly, speaks current date. If pressed thrice quickly, reports the current day, the week number, the current year and the days remaining before the end of the year."),
		category=globalCommands.SCRCAT_SYSTEM,
		gesture="kb:NVDA+f12"
	)
	def script_reportTimeAndDate(self, gesture):
		now = datetime.now()
		if scriptHandler.getLastScriptRepeatCount() == 0:
			msg = GetTimeFormatEx(None, None, now, formats.rgx.sub(formats.repl, formats.timeFormats[config.conf['clockAndCalendar']['timeDisplayFormat']]))
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			msg = GetDateFormatEx(None, None, None, formats.dateFormats[config.conf['clockAndCalendar']['dateDisplayFormat']])
		else:
			informations = getDayAndWeekOfYear(GetDateFormatEx(None, None, None, u"yyyy/M/d"))
			msg = _("Day {day}, week {week} of {year}, remaining days {remain}.").format(day=informations[0], week=informations[1], year=informations[2], remain=informations[3])
		ui.message(msg)
	# We remove the docstring from the original dateTime script to have only one entry in the "System status" category, it will be automatically restored if the Clock add-on is disabled or uninstalled.
	globalCommands.commands.script_dateTime.__func__.__doc__ = ""

	def getScript(self, gesture):
		if not hasattr(self, "clockLayerModeActive") or (hasattr(self, "clockLayerModeActive") and not self.clockLayerModeActive):
			return globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		script = globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		if not script:
			return self.script_error
		self.layeredScriptToRun = next((x[1] for x in self._clockLayerGestures if x[0] == gesture.mainKeyName), None)
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
		# Translators: Message presented in input help mode.
		description=_("Clock and calendar layer commands. After pressing this keystroke, press H for additional help."),
		gesture="kb:NVDA+shift+f12"
	)
	def script_clockLayerCommands(self, gesture):
		if self.clockLayerModeActive:
			self.script_error(gesture)
			return
		for gesture in self._clockLayerGestures:
			self.bindGesture("kb:%s" % gesture[0], gesture[1].__name__[7:])
		self.clockLayerModeActive = True
		tones.beep(100, 10)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Starts, resets or stops the stopwatch.")
	)
	def script_stopwatchRun(self, gesture):
		if not self.stopwatch.running and self.stopwatch.startTime:
			self.stopwatch.reset()
			self.stopwatch.start()
			ui.message(_("Reset. Running."))
		elif not self.stopwatch.running:
			self.stopwatch.start()
			ui.message(_("Running."))
		else:
			self.stopwatch.stop()
			ui.message(_(u"{0} stopped.").format(secondsToString(self.stopwatch.elapsedTime())))

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Speaks current stopwatch or count-down timer.")
	)
	def script_timeDisplay(self, gesture):
		ui.message(secondsToString(self.stopwatch.elapsedTime()))

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Gives the remaining and elapsed time before the next alarm.")
	)
	def script_alarmInfo(self, gesture):
		if alarmHandler.run and alarmHandler.run.is_alive():
			elapsedTime = alarmHandler.run.elapsed()
			remainingTime = alarmHandler.run.remaining()
			msg = _(u"Elapsed time {elapsed}, remaining time {remaining}.").format(elapsed=secondsToString(elapsedTime), remaining=secondsToString(remainingTime))
		else:
			msg = _("No alarm")
		ui.message(msg)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Cancel the next alarm.")
	)
	def script_cancelAlarm(self, gesture):
		if alarmHandler.run and alarmHandler.run.is_alive():
			alarmHandler.run.cancel()
			msg = _("Alarm cancelled")
		else:
			msg = _("No alarm")
		ui.message(msg)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Resets stopwatch to 0 without restarting it.")
	)
	def script_stopwatchReset(self, gesture):
		if self.stopwatch.startTime is None and self.stopwatch.stopTime is None and not self.stopwatch.running:
			ui.message(_("The stopwatch is already reset to 0. Use the clock layer command followed by s to start it."))
			return
		self.stopwatch.reset()
		ui.message(_("Stopwatch reset."))

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Lists available commands in clock command layer.")
	)
	def script_getHelp(self, gesture):
		ui.message("\n".join(x[0] + " : " + x[1].__doc__ if x[0] != "space" else skipTranslation.translate(x[0]) + " : " + x[1].__doc__ for x in self._clockLayerGestures))

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Allows to check the next alarm. If pressed twice, cancels it.")
	)
	def script_checkOrCancelAlarm(self, gestures):
		if alarmHandler.run and alarmHandler.run.is_alive():
			elapsedTime = alarmHandler.run.elapsed()
			remainingTime = alarmHandler.run.remaining()
			if scriptHandler.getLastScriptRepeatCount() > 0:
				alarmHandler.run.cancel()
				msg = _("Alarm cancelled")
			else:
				msg = _(u"Elapsed time {elapsed}, remaining time {remaining}.").format(elapsed=secondsToString(elapsedTime), remaining=secondsToString(remainingTime))
		else:
			msg = _("No alarm")
		ui.message(msg)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("If an alarm is too long, allows to stop it.")
	)
	def script_stopLongAlarm(self, gesture):
		msg = _("No sound is launched.")
		if nvwave.fileWavePlayer is not None:
			nvwave.fileWavePlayer.stop()
			msg = _("Sound stopped")
		ui.message(msg)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Display the clock settings dialog box.")
	)
	def script_activateClockSettingsDialog(self, gesture):
		wx.CallAfter(gui.mainFrame._popupSettingsDialog, gui.NVDASettingsDialog, ClockSettingsPanel)

	@scriptHandler.script(
		# Translators: Message presented in input help mode.
		description=_("Display the alarm settings dialog box.")
	)
	def script_activateAlarmSettingsDialog(self, gesture):
		wx.CallAfter(gui.mainFrame._popupSettingsDialog, gui.NVDASettingsDialog, AlarmSettingsPanel)
