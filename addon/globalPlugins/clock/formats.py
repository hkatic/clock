# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

import collections
import winKernel
import re
import addonHandler
addonHandler.initTranslation()

# This function has been taken up and modified from the latest versions of the WinKernel module to ensure compatibility of the GetTimeFormat function with the NVDA versions that preceded 2014.3.
def GetTimeFormat (Locale,dwFlags,date,lpFormat):
	"""@Deprecated: use GetTimeFormatEx instead."""
	from hwPortUtils import SYSTEMTIME
	import ctypes
	from ctypes import byref
	kernel32 = ctypes.windll.kernel32
	if date is not None:
		date=SYSTEMTIME(date.year,date.month,0,date.day,date.hour,date.minute,date.second,0)
		lpTime=byref(date)
	else:
		lpTime=None
	bufferLength=kernel32.GetTimeFormatW(Locale,dwFlags,lpTime,lpFormat, None, 0)
	buf=ctypes.create_unicode_buffer("", bufferLength)
	kernel32.GetTimeFormatW(Locale,dwFlags,lpTime,lpFormat, buf, bufferLength)
	return buf.value

if hasattr (winKernel, "GetTimeFormatEx") and hasattr(winKernel, "GetDateFormatEx"):
	GetTimeFormatEx = winKernel.GetTimeFormatEx
	GetDateFormatEx = winKernel.GetDateFormatEx
else:
	GetTimeFormatEx = winKernel.GetTimeFormat if hasattr (winKernel, "SYSTEMTIME") else GetTimeFormat
	GetDateFormatEx = winKernel.GetDateFormat

# A regular expression to match and facilitate translation for words that are not part of the formatting symbols.
ptrn=u"(\w+'?\w*|\$+[hmst]{1,2})"
rgx = re.compile (ptrn, re.U | re.I)

def repl (match):
	"""
	A function that captures and replaces words to make them compatible with the time format used in the GetTimeFormatEx function.
	@param match: The match obtained by the regular expression.
	@type match: basestring.
	@returns: The replaced captured group.
	@rtype: basestring.
	"""
	content = match.group(1)
	if content.startswith ("$"):
		return content.replace ("$", "")
	if "'" in content:
		return "'%s'" % content.replace ("'", "''")
	return "'%s'" % content

# The following function is not used yet.
def timeMarker ():
	"""
	A function that allows to find the time marker "AM" or "PM" for the formats of hours used in some English-speaking countries.
	As Windows defines this marker only if the regional language is English, this function allows to extend this to all other regions.
	@returns: The time marker am or pm corresponding to the current time.
	@rtype: basestring.
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

timeFormats = (
	# Translators: A time formating.
	_(u"It's {hours} o'clock and {minutes} minutes").format (hours = "$$H", minutes = "$$m"),
	# Translators: A time formating.
	_(u"It's {hours} o'clock, {minutes} minutes and {seconds} seconds").format (hours = "$$H", minutes = "$$m", seconds = "$$s"),
	# Translators: A time formating.
	_(u"{hours} o'clock, {minutes} minutes").format (hours = "$$h", minutes = "$$mm"),
	# Translators: A time formating.
	_(u"{hours} o'clock, {minutes} minutes, {seconds} seconds").format (hours = "$$h", minutes = "$$mm", seconds = "$$ss"),
	# Translators: A time formating.
	_(u"It's {minutes} past {hours}").format (minutes = "$$m", hours = "$$h"),
	# Translators: A time formating.
	_(u"{hours} h {minutes} min").format (hours = "$$h", minutes = "$$m"),
	# Translators: A time formating.
	_(u"{hours} h, {minutes} min, {seconds} sec").format (hours = "$$H", minutes = "$$m", seconds = "$$s"),
	# Translators: A time formating.
	_(u"It's {hours}:{minutes}").format (hours = "$$H", minutes = "$$m"),
	# Translators: A time formating.
	_(u"It's {hours}:{minutes}:{seconds}").format (hours = "$$HH", minutes = "$$mm", seconds = "$$ss"),
	u"$$hh:$$mm:$$ss $$tt",
	u"$$hh:$$m $$tt",
	u"$$hh:$$mm $$tt",
	u"$$h:$$mm $$tt",
	u"$$h:$$m:$$s",
	u"$$h:$$m $$tt",
	u"$$HH:$$mm",
	u"$$H:$$m:$$s",
	u"$$H:$$mm:$$ss",
	u"$$H:$$m",
)

timeFormatsDic = collections.OrderedDict()
for fmt in timeFormats:
	timeFormatsDic[fmt] = GetTimeFormatEx (None, None, None, rgx.sub(repl, fmt))

timeDisplayFormats = list(timeFormatsDic.values())

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

dateDisplayFormats = list (dateFormatsDic.values())
