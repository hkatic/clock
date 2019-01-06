# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

import config

confspec={
	'timeDisplayFormat': 'integer(default=0)',
	'dateDisplayFormat': 'integer(default=1)',
	'input24HourFormat': 'boolean(default=False)',
	'autoAnnounce': 'integer(default=0)',
	'timeReporting': 'integer(default=0)',
	'timeReportSound': 'string(default="clock_chime1.wav")',
	'alarmSound': 'string(default="alarm1.wav")',
	'alarmTimerChoice': 'integer(default=1)',
	'quietHours': 'boolean(default=False)',
	'alarmTime': 'float(default=0.0)',
	'alarmSavedTime': 'float(default=0.0)',
	'quietHoursStartTime': 'string(default="")',
	'quietHoursEndTime': 'string(default="")',
}
config.conf.spec["clockAndCalendar"]=confspec

