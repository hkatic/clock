# -*- coding: UTF-8 -*-

"""
Clock Add-on for NVDA
@author: Hrvoje Katić <hrvojekatic@gmail.com>
@license: GNU General Public License version 2.0
"""

_ = lambda x : x

addon_info = {
	"addon_name" : "clock",
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Clock"),
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""An advanced clock and calendar for NVDA.
Press NVDA + F12 for current time, press it twice for current date, or press it thrice to get current day and week of the year.
For other instructions, press Add-on help button in add-ons manager."""),
	"addon_version" : "1.0dev",
	"addon_author" : u"Hrvoje Katić <hrvojekatic@gmail.com>",
	"addon_url" : "https://www.bitbucket.org/HKatic/nvda-addon-clock",
	"addon_docFileName" : "readme.html",
}

import os.path

pythonSources = [os.path.join("addon", "globalPlugins", "clock", "*.py"), ]
i18nSources = pythonSources + ["buildVars.py"]
excludedFiles = []
