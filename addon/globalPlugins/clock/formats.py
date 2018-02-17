# -*- coding: utf-8 -*-

"""
Clock Add-on for NVDA
@author: Hrvoje Katich <hrvojekatic@gmail.com>
@license: GNU General Public License version 2.0
"""

import addonHandler
import datetime
import winKernel
import locale
addonHandler.initTranslation()

def isGregorianAndNotGeorgian (date):
		return datetime.datetime.now().strftime("%Y") in date and not locale.getdefaultlocale()[0] == u"ka_GE"

timeDisplayFormats = (
		datetime.datetime.now().strftime(_(u"It's {hours} hours and {minutes} minutes").format(hours="%H", minutes="%M")),
				datetime.datetime.now().strftime(_(u"It's {hours} hours, {minutes} minutes and {seconds} seconds").format(hours="%H", minutes="%M", seconds="%S")),
				datetime.datetime.now().strftime(_("{hours} hours, {minutes} minutes").format(hours="%H", minutes="%M")),
				datetime.datetime.now().strftime(_("{hours} hours, {minutes} minutes, {seconds} seconds").format(hours="%H", minutes="%M", seconds="%S")),
				datetime.datetime.now().strftime(_("{hours} h, {minutes} min").format(hours="%H", minutes="%M")),
				datetime.datetime.now().strftime(_("{hours} h, {minutes} min, {seconds} sec").format(hours="%H", minutes="%M", seconds="%S")),
						datetime.datetime.now().strftime("%H:%M:%S"),
								datetime.datetime.now().strftime("%H:%M"),
								datetime.datetime.now().strftime(_("It's {hours}:{minutes} {AM_PM}").format(hours="%I", minutes="%M", AM_PM="%p")),
								datetime.datetime.now().strftime(_("It's {hours}:{minutes}:{seconds} {AM_PM}").format(hours="%I", minutes="%M", seconds="%S", AM_PM="%p")),
										datetime.datetime.now().strftime("%I:%M %p"),
												datetime.datetime.now().strftime("%I:%M:%S %p")
	)

if isGregorianAndNotGeorgian (winKernel.GetDateFormat(winKernel.LOCALE_USER_DEFAULT, winKernel.DATE_LONGDATE, None, None)):
	dateDisplayFormats = (
				datetime.datetime.now().strftime("%A, %B %d, %Y"),
				datetime.datetime.now().strftime("%A %d %B %Y"),
				datetime.datetime.now().strftime("%Y-%d-%m"),
				datetime.datetime.now().strftime("%d-%m-%Y"),
				datetime.datetime.now().strftime("%m-%d-%Y"),
				datetime.datetime.now().strftime("%m/%d/%Y"),
				datetime.datetime.now().strftime("%d/%m/%Y")
	)
else:
	longDate = winKernel.GetDateFormat(winKernel.LOCALE_USER_DEFAULT, winKernel.DATE_LONGDATE, None, None).replace(",", "")
	dayOfWeek=day=month=year=""
	if "/" in longDate:
		day = longDate.split("/")[0]
		month = longDate.split("/")[1]
		year = longDate.split("/")[2]
	if len(longDate.split()) == 4:
		dayOfWeek = longDate.split()[0]
		day = longDate.split()[1]
		month = longDate.split()[2]
		year = longDate.split()[3]
	if len(longDate.split()) == 3:
		day = longDate.split()[0]
		month = longDate.split()[1]
		year = longDate.split()[2]
	dateDisplayFormats = (
	u"{dayOfWeek} {day} {month} {year}".format(dayOfWeek=dayOfWeek, day=day, month=month, year=year),
	u"{day} {month} {year}".format(day=day, month=month, year=year),
	u"{day}/{month}/{year}".format(day=day, month=month, year=year)
	)