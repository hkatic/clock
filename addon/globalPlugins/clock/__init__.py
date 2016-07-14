# -*- coding: utf-8 -*-

"""
Clock Add-on for NVDA
@author: Hrvoje Katich <hrvojekatic@gmail.com>
@license: GNU General Public License version 2.0
"""

import globalPluginHandler
import gui
import scriptHandler
import ui
import clockHandler
import clockSettingsGUI
import configuration
import config
from datetime import datetime
import wx
import gettext
import languageHandler
import addonHandler
addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super(globalPluginHandler.GlobalPlugin, self).__init__()
		self.prefsMenu = gui.mainFrame.sysTrayIcon.menu.GetMenuItems()[0].GetSubMenu()
		self.clockSettingsItem = self.prefsMenu.Append(wx.ID_ANY, _("&Clock Settings..."), _("Clock and calendar setup"))
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU , lambda evt: gui.mainFrame._popupSettingsDialog(clockSettingsGUI.clockSettingsDialog), self.clockSettingsItem)
		self.clock=clockHandler.clock()

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
	script_reportTimeAndDate.__doc__ = _(u"Speaks current time. If pressed twice quickly, speaks current date. If pressed thrice quickly, reports the current day and week number of the year.")

	__gestures={
		"kb:NVDA+f12": "reportTimeAndDate",
	}
