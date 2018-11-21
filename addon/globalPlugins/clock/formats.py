# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

import collections
import winKernel
import re
import addonHandler
addonHandler.initTranslation()
# A regular expression to match and facilitate translation for words that are not part of the formatting symbols.
ptrn=ur"(?<!')(\b(?!(?:h|hh|H|HH|m|mm|s|ss|t|tt)\b)\w+'?\w+)(?!')"
rgx = re.compile (ptrn, re.U)

def repl (match):
	content = match.group(1)
	if "'" in content:
		return "'%s'" % content.replace("'", "''")
	return "'%s'" % content

timeFormats = [
		_(u"It's H o'clock and mm minutes"),
		_(u"It's H o'clock, mm minutes and ss seconds"),
		_(u"h o'clock, mm minutes"),
		_(u"hh o'clock, mm minutes, ss seconds"),
		_(u"It's mm past H"),
		_(u"hh mm min"),
		_(u"hh mm min ss sec"),
		u"hh:mm:ss tt",
		u"hh:m tt",
		u"hh:mm tt",
		u"h:mm tt",
		u"h:m tt",
		_(u"It's H:mm"),
		_(u"It's HH:mm:ss"),
		u"HH:mm",
		u"H:mm"
	]

timeFormatsDic = collections.OrderedDict()
for fmt in timeFormats:
	timeFormatsDic[fmt] = winKernel.GetTimeFormatEx (winKernel.LOCALE_NAME_USER_DEFAULT, None, None, rgx.sub(repl, fmt))

timeDisplayFormats = timeFormatsDic.values()

dateFormats = [
		u"dddd, MMMM dd, yyyy",
		u"dddd dd MMMM yyyy",
		u"yyyy-dd-MM",
		u"yyyy-MM-dd",
		u"dd-MM-yyyy",
		u"MM-dd-yyyy",
		u"MM/dd/yyyy",
		u"dd/MM/yyyy"
	]

dateFormatsDic = collections.OrderedDict()
for fmt in dateFormats:
	dateFormatsDic[fmt] = winKernel.GetDateFormatEx (winKernel.LOCALE_NAME_USER_DEFAULT, None, None, fmt)
dateDisplayFormats = dateFormatsDic.values()