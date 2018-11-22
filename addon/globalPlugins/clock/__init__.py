# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

from functools import wraps
import sys
import globalPluginHandler
import gui
import scriptHandler
import ui
import winKernel
import formats
from gui import NVDASettingsDialog
import clockHandler
import stopwatchHandler
from clockSettingsGUI import ClockSettingsPanel
import configuration
import config
import tones
from datetime import datetime
import wx
import gettext
import os
import languageHandler
sys.path.append(os.path.join (os.path.abspath(os.path.dirname(__file__)), "lib"))
import ephem
import pytz
import convertdate
sys.path.remove(sys.path[-1])
import addonHandler
addonHandler.initTranslation()
import locale

#Command layer environment.
def finally_(func, final):
	"""Calls final after func, even if it fails."""
	def wrap(f):
		@wraps(f)
		def new(*args, **kwargs):
			try:
				func(*args, **kwargs)
			finally:
				final()
		return new
	return wrap(final)

#A function to convert seconds to user-friendly string, used for stopwatch and timer.
def secondsToString(seconds, precision=0):
	hour=seconds//3600
	min=(seconds//60)%60
	sec=seconds-(hour*3600)-(min*60)
	secSpec="."+str(precision)+"f"
	secString=sec.__format__(secSpec)
	string=""
	if(hour==1):
		string+=_("%d hour, ")%hour
	elif(hour>=2):
		string+=_("%d hours, ")%hour
	if(min==1):
		string+=_("%d minute, ")%min
	elif(min>=2):
		string+=_("%d minutes, ")%min
	if(sec==1):
		string+=_("%s second")%secString
	else:
		string+=_("%s seconds")%secString
	return string

# A function to calculate the current day of the year, as well as the actual number of weeks, for a non-Gregorian year.
def getDayAndWeekOfYear (date):
	now = datetime.now()
	curYear = int(date.split("/")[0])
	gregYear = int(now.strftime("%Y"))
	curMonth = int(date.split("/")[1])
	gregMonth = int(now.strftime("%m"))
	curDay = int(date.split("/")[2])
	gregDay = int(now.strftime("%d"))
	if curYear == gregYear:
		#It's a Gregorian year.
		return (now.timetuple()[7], now.isocalendar()[1], gregYear)
	else:
		# It's not a Gregorian year.
		dt1 = convertdate.islamic
		dt2 = convertdate.persian
		if curYear == dt1.from_gregorian(gregYear, gregMonth, gregDay)[0] or curYear == dt2.from_gregorian(gregYear, gregMonth, gregDay)[0]:
			# It's a Hijri year.
			dt = dt1 if curYear == dt1.from_gregorian(gregYear, gregMonth, gregDay)[0] else dt2
			nDayOfYear = 0
			nWeekOfYear = 0
			for month in xrange (1, curMonth):
				nDayOfYear += dt.month_length (curYear, month)
			nDayOfYear += curDay
			nWeekOfYear = nDayOfYear / 7
			if nDayOfYear % 7 > 0:
				nWeekOfYear += 1
			return (str(nDayOfYear), str(nWeekOfYear), str(curYear))

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: Script category for Clock addon commands in input gestures dialog.
	scriptCategory=_("Clock")

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		NVDASettingsDialog.categoryClasses.append(ClockSettingsPanel)
		self.clock=clockHandler.clock()
		self.stopwatch=stopwatchHandler.stopwatch()
		self.clockLayerModeActive=False

	def terminate(self):
		try:
			NVDASettingsDialog.categoryClasses.remove(ClockSettingsPanel)
		except wx.PyDeadObjectError:
			pass
		self.clock.terminate()

	def script_reportTimeAndDate(self, gesture):
		if scriptHandler.getLastScriptRepeatCount() == 0:
			msg=winKernel.GetTimeFormatEx(winKernel.LOCALE_NAME_USER_DEFAULT, None, None, formats.rgx.sub(formats.repl, config.conf["clockAndCalendar"]["timeDisplayFormat"]))
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			msg=winKernel.GetDateFormatEx(winKernel.LOCALE_NAME_USER_DEFAULT, None, None, config.conf["clockAndCalendar"]["dateDisplayFormat"])
		else:
			informations = getDayAndWeekOfYear (winKernel.GetDateFormatEx(winKernel.LOCALE_NAME_USER_DEFAULT, None, None, u"yyyy/M/d"))
			msg=_("Day {day}, week {week} of {year}").format(day=informations[0], week=informations[1], year=informations[2])
		ui.message(msg)
	script_reportTimeAndDate.__doc__=_("Speaks current time. If pressed twice quickly, speaks current date. If pressed thrice quickly, reports the current day and week number of the year.")

	def getScript(self, gesture):
		if not self.clockLayerModeActive:
			return globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		script=globalPluginHandler.GlobalPlugin.getScript(self, gesture)
		if not script:
			script=finally_(self.script_error, self.finish)
		return finally_(script, self.finish)

	def finish(self):
		self.clockLayerModeActive=False
		self.clearGestureBindings()
		self.bindGestures(self.__gestures)

	def script_error(self, gesture):
		tones.beep(120, 100)

	def script_clockLayerCommands(self, gesture):
		if self.clockLayerModeActive:
			self.script_error(gesture)
			return
		self.bindGestures(self.__clockLayerGestures)
		self.clockLayerModeActive=True
		tones.beep(100, 10)
	script_clockLayerCommands.__doc__=_("Clock and calendar layer commands. After pressing this keystroke, press H for additional help.")

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
			ui.message(_("%s stopped."%(secondsToString(self.stopwatch.elapsedTime()))))
	script_stopwatchRun.__doc__=_("Starts, stops or resets stopwatch.")

	def script_timeDisplay(self, gesture):
		ui.message(secondsToString(self.stopwatch.elapsedTime()))
	script_timeDisplay.__doc__=_("Speaks current stopwatch or timer countdown.")

	def script_stopwatchReset(self, gesture):
		if self.stopwatch.startTime == None and self.stopwatch.stopTime == None and self.stopwatch.running == False:
			ui.message(_("The stopwatch is already reset to 0. Use the clock layer command followed by s to start it."))
			return
		self.stopwatch.reset()
		ui.message(_("Stopwatch reset."))
	script_stopwatchReset.__doc__=_("Resets the stopwatch to 0 seconds, with out starting it.")

	def script_getHelp(self, gesture):
		ui.message(_("""
S: Start, stop or reset and restart the stopwatch.
R: Reset the stopwatch with out starting it again.
Spacebar: Speak current stopwatch or count-down timer."""))
	script_getHelp.__doc__=_("Lists available commands in clock command layer.")

	__clockLayerGestures={
		"kb:s":"stopwatchRun",
		"kb:space":"timeDisplay",
		"kb:r":"stopwatchReset",
		"kb:h":"getHelp",
	}
	def script_test(self, gestures):
		dt=convertdate.persian.from_gregorian(2018,11,19)
		ui.message(str(dt[0]))

	__gestures={
		"kb:NVDA+f12": "reportTimeAndDate",
		"kb:NVDA+shift+f12": "clockLayerCommands",
		"kb:control+f12": "test",
	}
