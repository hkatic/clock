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
Press NVDA + F12 for current time, press it twice for current date, or press it thrice to get current day and week of the year.
For other instructions, press Add-on help button in add-ons manager."""),
	"addon_version" : "18.05dev",
	"addon_author" : u"Hrvoje Katić <hrvojekatic@gmail.com>",
	"addon_url" : "https://github.com/hkatic/clock",
	"addon_docFileName" : "readme.html",
}

import os.path

pythonSources = [os.path.join("addon", "globalPlugins", "clock", "*.py"), ]
i18nSources = pythonSources + ["buildVars.py"]
excludedFiles = []
