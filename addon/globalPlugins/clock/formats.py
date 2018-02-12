# -*- coding: utf-8 -*-

"""
Clock Add-on for NVDA
@author: Hrvoje Katich <hrvojekatic@gmail.com>
@license: GNU General Public License version 2.0
"""

import addonHandler
addonHandler.initTranslation()

timeDisplayFormats = [
		_("It's %H hours and %M minutes"),
		_("It's %H hours, %M minutes and %S seconds"),
		_("%H hours, %M minutes"),
		_("%H hours, %M minutes, %S seconds"),
		_("%H h, %M min"),
		_("%H h, %M min, %S sec"),
		_("%H:%M:%S"),
		_("%H:%M"),
		_("It's %I:%M %p"),
		_("It's %I:%M:%S %p"),
		_("%I:%M %p"),
		_("%I:%M:%S %p")
	]

dateDisplayFormats = [
		"%A, %B %d, %Y",
		"%Y-%d-%m",
		"%d-%m-%Y",
		"%m-%d-%Y",
		"%m/%d/%Y",
		"%d/%m/%Y"
	]
