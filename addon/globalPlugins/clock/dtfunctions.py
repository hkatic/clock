# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

from datetime import datetime, timedelta

def parseTime(t, parse24hour=False):
	"""
	A function that can be used to convert a time format to a valid datetime.datetime object.
	@param t: The time format to convert in the H:mm or H:mm form.
	@type t: unicode or str.
	@param parse24hour: optional: A boolean to determine whether the required time format is a 24-hour format or not.
	@type parse24hours: boolean.
	@returns: The time format converted to datetime.datetime format.
	@rtype : datetime.datetime.
	"""
	f=''
	if parse24hour:
		f='%H:%M'
	else:
		f='%I:%M %p'
	return datetime.strptime(t, f)

def strfNowTime(parse24hour=False):
	"""
	A function that converts the current date format to a simple string.
	@param parse24hour: optional: A boolean to determine whether the required time format is a 24-hour format or not
	@type parse24hours: boolean.
	@returns : The current time format converted to a string.
	@rtype: unicode or str.
	"""
	f=''
	if parse24hour:
		f='%H:%M'
	else:
		f='%I:%M %p'
	return datetime.now().strftime(f)

def timeInRange(startTime, endTime, checkTime, use24hour=False):
	"""
	A function that can be used to check whether the time range received as a parameter does not match a specific time.
	@param startTime: The start time in the range.
	@type startTime: unicode or str.
	@param endTime: The end time in the range.
	@type endTime: unicode or str.
	@param checkTime: The time that will allow for the verification.
	@type checkTime: unicode or str.
	@param use24hour: optional: A boolean to determine whether the specified times format are 24-hour format or not.
	@type use24hours: boolean.
	@returns: A Boolean corresponding to the verification.
	@rtype: boolean.
	"""
	
	start=parseTime(startTime, use24hour)
	end=parseTime(endTime, use24hour)
	if end<start:
		end+=timedelta(days=1)
	check=parseTime(checkTime, use24hour)
	return start<=check<end
