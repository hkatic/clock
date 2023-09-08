# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

import winKernel
import re
from datetime import datetime
import addonHandler
addonHandler.initTranslation()

# A regular expression to match and facilitate translation for words that are
# not part of the formatting symbols.
ptrn = r"(\w+'?\w*|\$+[hmst]{1,2})"
rgx = re.compile(ptrn, re.U | re.I)

# An example date/time
# This example should have single digit for hours, minutes and seconds so that one and two digit formats
# are distinguishable.
DT_EXAMPLE = datetime(2022, 6, 2, 1, 5, 9)

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
	tm = ""
	dt = int(datetime.now().strftime("%H"))
	if dt > 12:
		tm = "pm"
	else:
		if dt < 12 and dt > 0:
			tm = "am"
	return tm

def is24HourFormat(fmt):
	"""
	A function that indicates if a time format is a 24-hour format.
	@param fmt: A time format.
	@type fmt: basestring.
	@returns: True if the time format is a 24-hour format, False if it is a 12-hour format.
	@rtype: bool.
	"""
	return "$$H" in fmt
	

timeFormats = (
	# Translators: A time formating (should be different from other time formattings)
	_("It's {hours} o'clock and {minutes} minutes").format(hours="$$H", minutes="$$m"),
	# Translators: A time formating (should be different from other time formattings)
	_("It's {hours} o'clock, {minutes} minutes and {seconds} seconds").format(
		hours="$$H", minutes="$$m", seconds="$$s"
	),
	# Translators: A time formating (should be different from other time formattings)
	_("{hours} o'clock, {minutes} minutes").format(hours="$$H", minutes="$$mm"),
	# Translators: A time formating (should be different from other time formattings)
	_("{hours} o'clock, {minutes} minutes, {seconds} seconds").format(
		hours="$$H", minutes="$$mm", seconds="$$ss"
	),
	# Translators: A time formating (should be different from other time formattings)
	_("It's {minutes} past {hours}").format(minutes="$$m", hours="$$H"),
	# Translators: A time formating (should be different from other time formattings)
	_("{hours} h {minutes} min").format(hours="$$H", minutes="$$m"),
	# Translators: A time formating (should be different from other time formattings)
	_("{hours} h, {minutes} min, {seconds} sec").format(hours="$$H", minutes="$$m", seconds="$$s"),
	# Translators: A time formating (should be different from other time formattings)
	_("It's {hours}:{minutes}").format(hours="$$H", minutes="$$m"),
	# Translators: A time formating (should be different from other time formattings)
	_("It's {hours}:{minutes}:{seconds}").format(hours="$$HH", minutes="$$mm", seconds="$$ss"),
	"$$hh:$$mm:$$ss $$tt",
	"$$hh:$$m $$tt",
	"$$hh:$$mm $$tt",
	"$$h:$$mm $$tt",
	"$$H:$$m:$$s $$tt",
	"$$h:$$m $$tt",
	"$$HH:$$mm",
	"$$H:$$m:$$s",
	"$$H:$$mm:$$ss",
    "$$H $$mm $$ss",
    "$$HH $$mm $$ss",
	"$$H:$$m",
)

timeDisplayFormats = [(
	# Translators: A way to display 24-hour formats in the time display formats list in the settings panel.
	_('{fmt} (24-hour format)') if is24HourFormat(fmt) else
	# Translators: A way to display 12-hour formats in the time display formats list in the settings panel.
	_('{fmt} (12-hour format)')
).format(fmt=winKernel.GetTimeFormatEx(None, None, DT_EXAMPLE, rgx.sub(repl, fmt))) for fmt in timeFormats]

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

dateDisplayFormats = [winKernel.GetDateFormatEx(None, None, None, fmt) for fmt in dateFormats]
