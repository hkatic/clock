# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

from datetime import datetime, timedelta

def parseTime(t, parse24hour=False):
	f=''
	if parse24hour:
		f='%H:%M'
	else:
		f='%I:%M %p'
	return datetime.strptime(t, f)

def strfNowTime(parse24hour=False):
	f=''
	if parse24hour:
		f='%H:%M'
	else:
		f='%I:%M %p'
	return datetime.now().strftime(f)

def timeInRange(startTime, endTime, checkTime, use24hour=False):
	start=parseTime(startTime, use24hour)
	end=parseTime(endTime, use24hour)
	if end<start:
		end+=timedelta(days=1)
	check=parseTime(checkTime, use24hour)
	return start<=check<end
