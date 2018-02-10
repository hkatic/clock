# -*- coding: utf-8 -*-

"""
Clock Add-on for NVDA
@author: Hrvoje Katich <hrvojekatic@gmail.com>
@license: GNU General Public License version 2.0
"""

from functools import wraps
import globalPluginHandler
import gui
import scriptHandler
import ui
import clockHandler
import stopwatchHandler
import clockSettingsGUI
import configuration
import config
import tones
from datetime import datetime
import wx
import gettext
import languageHandler
import addonHandler
addonHandler.initTranslation()

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

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.prefsMenu=gui.mainFrame.sysTrayIcon.menu.GetMenuItems()[0].GetSubMenu()
		self.clockSettingsItem=self.prefsMenu.Append(wx.ID_ANY, _("&Clock Settings..."), _("Clock and calendar setup"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU , lambda evt: gui.mainFrame._popupSettingsDialog(clockSettingsGUI.clockSettingsDialog), self.clockSettingsItem)
		self.clock=clockHandler.clock()
		self.stopwatch=stopwatchHandler.stopwatch()
		self.clockLayerModeActive=False

	def terminate(self):
		try:
			self.prefsMenu.RemoveItem(self.clockSettingsItem)
		except wx.PyDeadObjectError:
			pass
		self.clock.terminate()

	def script_reportTimeAndDate(self, gesture):
		if scriptHandler.getLastScriptRepeatCount() == 0:
			ui.message(datetime.now().strftime(config.conf["clockAndCalendar"]["timeDisplayFormat"]).decode("mbcs"))
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.message(datetime.now().strftime(config.conf["clockAndCalendar"]["dateDisplayFormat"]).decode("mbcs"))
		else:
			ui.message(datetime.now().strftime("Day %j, week %W of %Y."))
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

	__gestures={
		"kb:NVDA+f12": "reportTimeAndDate",
		"kb:NVDA+shift+f12": "clockLayerCommands",
	}
