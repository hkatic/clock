	# -*- coding: UTF-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

_ = lambda x : x

addon_info = {
	"addon_name" : "clock",
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Clock"),
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""An advanced clock and calendar for NVDA.
NVDA+F12, get current time.
NVDA+F12 pressed twice quickly, get current date.
NVDA+F12 pressed thrice quickly, reports the current day, the week number, the current year and the remaining days before the end of the year.
For other instructions, press Add-on help button in add-ons manager."""),
	"addon_version" : "19.09-dev",
	"addon_author" : "Hrvoje Katic <hrvojekatic@gmail.com>, Abdel <abdelkrim.bensaid@gmail.com>",
	"addon_url" : "https://github.com/hkatic/clock",
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3")
	"addon_minimumNVDAVersion" : "2014.3.0",
	# Last NVDA version supported/tested (e.g. "2018.4", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2019.4.0",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : None,
}

import os.path

pythonSources = [os.path.join("addon", "*.py"), os.path.join("addon", "globalPlugins", "clock", "*.py")]
i18nSources = pythonSources + ["buildVars.py"]
excludedFiles = []
