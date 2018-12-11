# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

import config
import addonHandler
addonHandler.initTranslation()

def onInstall ():
	import gui
	import wx
	if not next ((x.isdigit () for x in (config.conf['clockAndCalendar']['timeDisplayFormat'], config.conf['clockAndCalendar']['dateDisplayFormat'])), False):
		if gui.messageBox(
			# Translators: the label of a message box dialog.
			_("The date and time format you were using are not compatible with this version of the Clock add-on, this will be fixed during installation. Click OK to confirm these corrections"),
			# Translators: the title of a message box dialog.
			_("Time and date format corrections"), wx.OK | wx.ICON_INFORMATION
			) == wx.OK:
				config.conf['clockAndCalendar']['timeDisplayFormat'] = 0
				config.conf['clockAndCalendar']['dateDisplayFormat'] = 1

