# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

import config
from configobj.validate import VdtTypeError
import addonHandler
addonHandler.initTranslation()


def onInstall():
	import gui
	import wx
	addon = next((addon for addon in addonHandler.getRunningAddons() if addon.name == "clock"), None)
	curProfile = config.conf.profiles[0]
	if addon and addon.version < "31.08.1":
		# We're migrating from a version that doesn't support 5-minute intervals; therefore, we must update the configuration key value.
		if config.conf["clockAndCalendar"]["autoAnnounce"] > 0:
			config.conf["clockAndCalendar"]["autoAnnounce"]+= 1
			# For those who have not checked the "Save configuration on exit" checkbox.
			if not config.conf["general"]["saveConfigurationOnExit"]:
				config.conf.save()
	if (
		'clockAndCalendar' in curProfile and (
			'timeDisplayFormat' in list(curProfile['clockAndCalendar'].keys())
			and not isinstance(config.conf['clockAndCalendar']['timeDisplayFormat'], int))
	):
		if gui.messageBox(
			_(
				# Translators: the label of a message box dialog.
				"The date and time format you were using are not compatible with this version of the Clock add-on, "
				"this will be fixed during installation. Click OK to confirm these corrections"
			),
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
					config.conf.save()
