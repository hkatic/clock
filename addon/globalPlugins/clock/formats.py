# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

import collections
import winKernel
import re
import addonHandler
addonHandler.initTranslation()

# A regular expression to match and facilitate translation for words that are
# not part of the formatting symbols.
# Ignore Flake8 W605: invalid escape sequence (\w)
ptrn = "(\w+'?\w*|\$+[hmst]{1,2})"  # NOQA: W605
rgx = re.compile(ptrn, re.U | re.I)


def repl(match):
	"""
	A function that captures and replaces words to make them
	compatible with the time format used in the GetTimeFormatEx function.
	@param match: The match obtained by the regular expression.
	@type match: basestring.
	@returns: The replaced captured group.
	@rtype: basestring.
	"""
	content = match.group(1)
	if content.startswith("$"):
		return content.replace("$", "")
	if "'" in content:
		return "'%s'" % content.replace("'", "''")
	return "'%s'" % content


# The following function is not used yet.
def timeMarker():
	"""
	A function that allows to find the time marker "AM" or "PM"
	for the formats of hours used in some English-speaking countries.
	As Windows defines this marker only if the regional language is English,
	this function allows to extend this to all other regions.
	@returns: The time marker am or pm corresponding to the current time.
	@rtype: basestring.
	"""
	from datetime import datetime
	tm = ""
	dt = int(datetime.now().strftime("%H"))
	if dt > 12:
		tm = "pm"
	else:
		if dt < 12 and dt > 0:
			tm = "am"
	return tm


timeFormats = (
	# Translators: A time formating.
	_("It's {hours} o'clock and {minutes} minutes").format(hours="$$H", minutes="$$m"),
	# Translators: A time formating.
	_("It's {hours} o'clock, {minutes} minutes and {seconds} seconds").format(
		hours="$$H", minutes="$$m", seconds="$$s"
	),
	# Translators: A time formating.
	_("{hours} o'clock, {minutes} minutes").format(hours="$$H", minutes="$$mm"),
	# Translators: A time formating.
	_("{hours} o'clock, {minutes} minutes, {seconds} seconds").format(
		hours="$$H", minutes="$$mm", seconds="$$ss"
	),
	# Translators: A time formating.
	_("It's {minutes} past {hours}").format(minutes="$$m", hours="$$H"),
	# Translators: A time formating.
	_("{hours} h {minutes} min").format(hours="$$H", minutes="$$m"),
	# Translators: A time formating.
	_("{hours} h, {minutes} min, {seconds} sec").format(hours="$$H", minutes="$$m", seconds="$$s"),
	# Translators: A time formating.
	_("It's {hours}:{minutes}").format(hours="$$H", minutes="$$m"),
	# Translators: A time formating.
	_("It's {hours}:{minutes}:{seconds}").format(hours="$$HH", minutes="$$mm", seconds="$$ss"),
	"$$hh:$$mm:$$ss $$tt",
	"$$hh:$$m $$tt",
	"$$hh:$$mm $$tt",
	"$$h:$$mm $$tt",
	"$$H:$$m:$$s",
	"$$h:$$m $$tt",
	"$$HH:$$mm",
	"$$H:$$m:$$s",
	"$$H:$$mm:$$ss",
	"$$H:$$m",
)

timeFormatsDic = collections.OrderedDict()
for fmt in timeFormats:
	timeFormatsDic[fmt] = winKernel.GetTimeFormatEx(None, None, None, rgx.sub(repl, fmt))

timeDisplayFormats = list(timeFormatsDic.values())

dateFormats = (
	"dddd, MMMM dd, yyyy",
	"dddd dd MMMM yyyy",
	"yyyy-dd-MM",
	"d/M/yy",
	"d/M/yyyy",
	"yyyy-MM-dd",
	"dd-MM-yyyy",
	"MM-dd-yyyy",
	"MM/dd/yyyy",
	"dd/MM/yyyy"
)

dateFormatsDic = collections.OrderedDict()
for fmt in dateFormats:
	dateFormatsDic[fmt] = winKernel.GetDateFormatEx(None, None, None, fmt)

dateDisplayFormats = list(dateFormatsDic.values())
