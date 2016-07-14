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
			ui.message(datetime.now().strftime(config.conf["clockAndCalendar"]["timeDisplayFormat"]))
		elif scriptHandler.getLastScriptRepeatCount() == 1:
			ui.message(datetime.now().strftime(config.conf["clockAndCalendar"]["dateDisplayFormat"]))
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

	def script_stopwatchStart(self, gesture):
		self.stopwatch.start()
		ui.message(_("Stopwatch running."))
	script_stopwatchStart.__doc__=_("Starts stopwatch.")

	def script_stopwatchReset(self, gesture):
		self.stopwatch.reset()
		ui.message(_("Stopwatch reset."))
	script_stopwatchReset.__doc__=_("Resets stopwatch.")

	def script_stopwatchStop(self, gesture):
		self.stopwatch.stop()
		ui.message(_("Stopwatch stopped."))
	script_stopwatchStop.__doc__=_("Stops stopwatch.")

	def script_timeDisplay(self, gesture):
		display=secondsToString(self.stopwatch.elapsedTime())
		ui.message(display)
	script_timeDisplay.__doc__=_("Speaks current stopwatch or timer countdown.")

	def script_getHelp(self, gesture):
		ui.message(_("""
W: Stopwatch start.
R: Stopwatch reset.
S: Stopwatch stop.
Spacebar: Speak current stopwatch or count-down timer."""))
	script_getHelp.__doc__=_("Lists available commands in clock command layer.")

	__clockLayerGestures={
		"kb:w":"stopwatchStart",
		"kb:r":"stopwatchReset",
		"kb:s":"stopwatchStop",
		"kb:space":"timeDisplay",
		"kb:h":"getHelp",
	}

	__gestures={
		"kb:NVDA+f12": "reportTimeAndDate",
		"kb:NVDA+shift+f12": "clockLayerCommands",
	}
