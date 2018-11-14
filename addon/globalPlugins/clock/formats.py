# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.
import collections
import winKernel
import addonHandler
addonHandler.initTranslation()

timeFormats = [
		_(u"'It''s' H 'o''clock' and mm 'minutes'"),
		_(u"'It''s' H 'o''clock', mm 'minutes' and ss 'seconds'"),
		_(u"h 'o''clock', mm 'minutes'"),
		_(u"hh 'o''clock', mm 'minutes', ss 'seconds'"),
		_(u"'It''s' mm 'past' H"),
		_(u"hh 'h', mm 'min'"),
		_(u"hh 'h', mm 'min', ss 'sec'"),
		u"hh:mm:ss",
		u"hh:mm",
		_(u"'It''s' H:mm"),
		_(u"'It''s' HH:mm:ss"),
		u"HH:mm"
	]

timeFormatsDic = collections.OrderedDict()
for fmt in timeFormats:
	timeFormatsDic[fmt] = winKernel.GetTimeFormatEx (winKernel.LOCALE_NAME_USER_DEFAULT, None, None, fmt)

timeDisplayFormats = timeFormatsDic.values()

dateFormats = [
		u"dddd, MMMM dd, yyyy",
		u"dddd dd MMMM yyyy",
		u"yyyy-dd-MM",
		u"yyyy-MM-dd",
		u"dd-MM-yyyy",
		u"MM-dd-yyyy",
		u"MM/dd/yyyy",
		u"dd/MM/yyyy"
	]

dateFormatsDic = collections.OrderedDict()
for fmt in dateFormats:
	dateFormatsDic[fmt] = winKernel.GetDateFormatEx (winKernel.LOCALE_NAME_USER_DEFAULT, None, None, fmt)
dateDisplayFormats = dateFormatsDic.values()