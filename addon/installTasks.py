# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

import config
from validate import VdtTypeError
import addonHandler
addonHandler.initTranslation()

def onInstall ():
	import gui
	import wx
	curProfile = config.conf.profiles[0]
	if curProfile.has_key ('clockAndCalendar') and ('timeDisplayFormat' in list(curProfile['clockAndCalendar'].keys ()) and not isinstance (config.conf['clockAndCalendar']['timeDisplayFormat'], int)):
		if gui.messageBox(
			# Translators: the label of a message box dialog.
			_("The date and time format you were using are not compatible with this version of the Clock add-on, this will be fixed during installation. Click OK to confirm these corrections"),
			# Translators: the title of a message box dialog.
			_("Time and date format corrections"), wx.OK | wx.ICON_INFORMATION
			) == wx.OK:
				try:
					config.conf['clockAndCalendar']['timeDisplayFormat'] = 0
					config.conf['clockAndCalendar']['dateDisplayFormat'] = 1
				except VdtTypeError:
					config.conf['clockAndCalendar']['timeDisplayFormat'] = "0"
					config.conf['clockAndCalendar']['dateDisplayFormat'] = "1"
				finally:
					# For those who have not checked the "Save configuration on exit" checkbox.
					if not config.conf["general"]["saveConfigurationOnExit"]:
						config.conf.save ()
