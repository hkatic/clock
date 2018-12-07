# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

import config

confspec={
	'timeDisplayFormat': 'string(default="%H:%M")',
	'dateDisplayFormat': 'string(default="%m/%d/%Y")',
	'input24HourFormat': 'boolean(default=False)',
	'autoAnnounce': 'integer(default=0)',
	'timeReporting': 'integer(default=0)',
	'timeReportSound': 'string(default="clock_chime1.wav")',
	'alarmSound': 'string(default="clock_chime1.wav")',
	'alarmTimerChoice': 'integer(default=1)',
	'quietHours': 'boolean(default=False)',
	'alarmTime': 'string(default="")',
	'quietHoursStartTime': 'string(default="")',
	'quietHoursEndTime': 'string(default="")',
}
config.conf.spec["clockAndCalendar"]=confspec
