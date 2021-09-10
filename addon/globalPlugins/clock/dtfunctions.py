# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

from datetime import datetime, timedelta
from typing import Optional


def convertTo24Hour(hr: str) -> str:
	"""
	A function for converting a 12-hour time format to 24-hour time format.
	This will facilitate the use of AM/PM suffixed hour formats in all locale time formats,
	including those that do not use this type of format.
	This type of input will then be used when entering quiet hours in the 12-hour format.
	@param hr: The 12-hour time format that includes the AM or PM suffix to be converted to 24-hour format.
	@type hr: basestring.
	@returns: The time format converted to 24-hour format.
	@rtype: basestring.
	"""
	now = datetime.now()
	is12h = False
	h = hr.split(":")[0]
	if hr[-2:] in ("AM", "am", "PM", "pm"):
		is12h = True
		end = hr[len(h):-3]
	else:
		end = hr[len(h):len(h) + 3]
	if is12h:
		p = hr[-2:]
		res = str(int(h) + 12) if p in ("pm", "PM") else h
	else:
		res = str(int(h) + 12) if int(now.strftime("%H")) > 12 else h
	res = res + end if res != "24" else "0" + end
	return res


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
