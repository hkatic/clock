# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

import collections
import winKernel
import re
import addonHandler
addonHandler.initTranslation()

if hasattr (winKernel, "GetTimeFormatEx") and hasattr(winKernel, "GetDateFormatEx"):
	GetTimeFormatEx = winKernel.GetTimeFormatEx
	GetDateFormatEx = winKernel.GetDateFormatEx
else:
	GetTimeFormatEx = winKernel.GetTimeFormat
	GetDateFormatEx = winKernel.GetDateFormat

# A regular expression to match and facilitate translation for words that are not part of the formatting symbols.
ptrn=ur"(\w+'?\w*|\$+[hmst]{1,2})"
rgx = re.compile (ptrn, re.U | re.I)

def repl (match):
	"""
	A function that captures and replaces words to make them compatible with the time format used in the GetTimeFormatEx function.
	@param match: The match obtained by the regular expression
	@type match: unicode or str
	@returns: The captured group replaced
	@rtype: unicode or str
	"""
	content = match.group(1)
	if content.startswith ("$"):
		return content.replace ("$", "")
	if "'" in content:
		return "'%s'" % content.replace ("'", "''")
	return "'%s'" % content

def timeMarker ():
	"""
	A function that allows to find the time marker "AM" or "PM" for the formats of hours used in some English-speaking countries.
	As Windows defines this marker only if the regional language is English, this function allows to extend this to all other regions.
	@returns: The time marker am or pm corresponding to the current time.
	@rtype: unicode or str.
	"""
	from datetime import datetime
	tm = ""
	dt = int(datetime.now ().strftime ("%H"))
	if dt > 12:
		tm = u"pm"
	else:
		if dt < 12 and dt > 0:
			tm = u"am"
	return tm

timeFormatsConfig = (
	("It's H o'clock and m minutes",
	# Translators: A time formating.
	_(u"It's {hours} o'clock and {minutes} minutes").format (hours = "$$H", minutes = "$$m")),
	("It's H o'clock, m minutes and s seconds",
	# Translators: A time formating.
	_(u"It's {hours} o'clock, {minutes} minutes and {seconds} seconds").format (hours = "$$H", minutes = "$$m", seconds = "$$s")),
	("h o'clock, mm minutes",
	# Translators: A time formating.
	_(u"{hours} o'clock, {minutes} minutes").format (hours = "$$h", minutes = "$$mm")),
	("h o'clock, mm minutes, ss seconds",
	# Translators: A time formating.
	_(u"{hours} o'clock, {minutes} minutes, {seconds} seconds").format (hours = "$$h", minutes = "$$mm", seconds = "$$ss")),
	("It's m past h tt",
	# Translators: A time formating.
	_(u"It's {minutes} past {hours} {tm}").format (minutes = "$$m", hours = "$$h", tm = timeMarker ())),
	("h h m min",
	# Translators: A time formating.
	_(u"{hours} h {minutes} min").format (hours = "$$h", minutes = "$$m")),
	("H h, m min, s sec",
	# Translators: A time formating.
	_(u"{hours} h, {minutes} min, {seconds} sec").format (hours = "$$H", minutes = "$$m", seconds = "$$s")),
	("It's H:m",
	# Translators: A time formating.
	_(u"It's {hours}:{minutes}").format (hours = "$$H", minutes = "$$m")),
	("It's HH:mm:ss",
	# Translators: A time formating.
	_(u"It's {hours}:{minutes}:{seconds}").format (hours = "$$HH", minutes = "$$mm", seconds = "$$ss")),
	("hh:mm:ss tt",
	u"$$hh:$$mm:$$ss {tm}".format (tm = timeMarker ())),
	("hh:m tt",
	u"$$hh:$$m {tm}".format (tm = timeMarker ())),
	("hh:mm tt",
	u"$$hh:$$mm {tm}".format (tm = timeMarker ())),
	("h:mm tt",
	u"$$h:$$mm {tm}".format (tm = timeMarker ())),
	("h:m:s",
	u"$$h:$$m:$$s"),
	("h:m tt",
	u"$$h:$$m {tm}".format (tm = timeMarker ())),
	("HH:mm",
	u"$$HH:$$mm"),
	("H:m:s",
	u"$$H:$$m:$$s"),
	("H:m",
	u"$$H:$$m"),
)

timeFormats = tuple (x[1] for x in timeFormatsConfig)

timeFormatsDic = collections.OrderedDict()
for fmt in timeFormats:
	timeFormatsDic[fmt] = GetTimeFormatEx (None, None, None, rgx.sub(repl, fmt))

timeDisplayFormats = timeFormatsDic.values()

dateFormats = (
	u"dddd, MMMM dd, yyyy",
	u"dddd dd MMMM yyyy",
	u"yyyy-dd-MM",
	u"d/M/yy",
	u"d/M/yyyy",
	u"yyyy-MM-dd",
	u"dd-MM-yyyy",
	u"MM-dd-yyyy",
	u"MM/dd/yyyy",
	u"dd/MM/yyyy"
)

dateFormatsDic = collections.OrderedDict()
for fmt in dateFormats:
	dateFormatsDic[fmt] = GetDateFormatEx (None, None, None, fmt)

dateDisplayFormats = dateFormatsDic.values()
