# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

from datetime import datetime, timedelta
from typing import Optional


def convertTo24Hour(hr: str) -> str:
	"""
	A function for converting a 12-hour time format to 24-hour time format.
	String must be of the form hh:mm period.
	This will facilitate the use of AM/PM suffixed hour formats in all locale time formats,
	including those that do not use this type of format.
	This type of input will then be used when entering quiet hours in the 12-hour format.
	@param hr: The 12-hour time format that includes the AM or PM suffix to be converted to 24-hour format.
	@type hr: basestring.
	@returns: The time format converted to 24-hour format.
	@rtype: basestring.
	"""
	period = hr[-2:]
	am = period in ("AM", "am")
	pm = period in ("PM", "pm")
	is12h = am or pm
	if is12h:
		hm = hr.partition(" ")[0]
		hour, minute = [int(part) for part in hm.split(":")]
	else:
		hour, minute = [int(part) for part in hr.split(":")]
	if (am and hour == 12) or (not is12h and hour == 24):
		hour = 0
	elif pm and hour < 12:
		hour += 12
	return f"{hour:02d}:{minute:02d}"


def parseTime(t: str, parse24hour: Optional[bool] = False) -> datetime:
	"""
	A function that can be used to convert a time format to a valid datetime.datetime object.
	@param t: The time format to convert in the H:mm or H:mm form.
	@type t: basestring.
	@param parse24hour: optional: A boolean to determine whether the required time format is
	a 24-hour format or not.
	@type parse24hours: boolean.
	@returns: The time format converted to datetime.datetime format.
	@rtype : datetime.datetime.
	"""
	f = '%H:%M'
	if parse24hour:
		res = datetime.strptime(t, f)
	else:
		res = datetime.strptime(convertTo24Hour(t), f)
	return res


def strfNowTime(parse24hour: Optional[bool] = False) -> str:
	"""
	A function that converts the current date format to a simple string.
	@param parse24hour: optional: A boolean to determine whether the required time format
	is a 24-hour format or not
	@type parse24hours: boolean.
	@returns : The current time format converted to a string.
	@rtype: basestring.
	"""
	f = ''
	if parse24hour:
		f = '%H:%M'
	else:
		f = '%I:%M %p'
	return datetime.now().strftime(f)


def timeInRange(startTime: str, endTime: str, checkTime: str, use24hour: Optional[bool] = False) -> bool:
	"""
	A function that can be used to check whether the time range
	received as a parameter does not match a specific time.
	@param startTime: The start time in the range.
	@type startTime: basestring.
	@param endTime: The end time in the range.
	@type endTime: basestring.
	@param checkTime: The time that will allow for the verification.
	@type checkTime: basestring.
	@param use24hour: optional: A boolean to determine whether the specified times format
	are 24-hour format or not.
	@type use24hours: boolean.
	@returns: A Boolean corresponding to the verification.
	@rtype: boolean.
	"""
	start = parseTime(startTime, use24hour)
	end = parseTime(endTime, use24hour)
	check = parseTime(checkTime, use24hour)
	if end < start:
		end += timedelta(days=1)
		if check < start:
			check += timedelta(days=1)
	return start <= check < end
