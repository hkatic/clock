# -*- coding: utf-8 -*-

"""
Clock Add-on for NVDA
@author: Hrvoje Katich <hrvojekatic@gmail.com>
@license: GNU General Public License version 2.0
"""

import config

confspec={
	'timeDisplayFormat': 'string(default="%H:%M")',
	'dateDisplayFormat': 'string(default="%m/%d/%Y")',
	'input24HourFormat': 'boolean(default=False)',
	'autoAnnounce': 'integer(default=0)',
	'timeReporting': 'integer(default=0)',
	'timeReportSound': 'string(default="clock_chime1.wav")',
	'quietHours': 'boolean(default=False)',
	'quietHoursStartTime': 'string(default="")',
	'quietHoursEndTime': 'string(default="")',
}
config.conf.spec["clockAndCalendar"]=confspec
