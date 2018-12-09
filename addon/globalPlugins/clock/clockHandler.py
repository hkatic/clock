# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

from datetime import datetime
import dtfunctions
import paths
import config
import nvwave
import ui
import os
import wx
import formats
from formats import GetTimeFormatEx

def getAutoAnnounceInterval():
	autoAnnounceMinutes = tuple()
	autoAnnounce=config.conf["clockAndCalendar"]["autoAnnounce"]
	if autoAnnounce == 1:
		autoAnnounceMinutes = (0, 10, 20, 30, 40, 50)
	elif autoAnnounce == 2:
		autoAnnounceMinutes = (0, 15, 30, 45)
	elif autoAnnounce == 3:
		autoAnnounceMinutes = (0, 30)
	elif autoAnnounce == 4:
		autoAnnounceMinutes = (0, 0)
	return autoAnnounceMinutes

class clock(object):

	def __init__(self):
		self._autoAnnounceClockTimer = wx.PyTimer(self._handleClockAnnouncement)
		self._autoAnnounceClockTimer.Start(1000)

	def terminate(self):
		try:
			self._autoAnnounceClockTimer.Stop()
			del self._autoAnnounceClockTimer
		except:
			pass

	def _handleClockAnnouncement(self):
		if datetime.now().minute in getAutoAnnounceInterval() and datetime.now().second == 0:
			self.reportClock()

	def reportClock(self):
		if self.quietHoursAreActive():
			return
		if config.conf["clockAndCalendar"]["timeReporting"]!=1:
			nvwave.playWaveFile(os.path.join(paths.SOUNDS_DIR, config.conf["clockAndCalendar"]["timeReportSound"]))
		if config.conf["clockAndCalendar"]["timeReporting"]!=2:
			ui.message(GetTimeFormatEx (None, None, None, formats.rgx.sub(formats.repl, next (x[1] for x in formats.timeFormatsConfig if x[0] == config.conf["clockAndCalendar"]["timeDisplayFormat"]))))

	def quietHoursAreActive(self):
		if not config.conf["clockAndCalendar"]["quietHours"]:
			return False
		qhStartTime=config.conf["clockAndCalendar"]["quietHoursStartTime"]
		qhEndTime=config.conf["clockAndCalendar"]["quietHoursEndTime"]
		nowTime=dtfunctions.strfNowTime(config.conf["clockAndCalendar"]["input24HourFormat"])
		if dtfunctions.timeInRange(qhStartTime, qhEndTime, nowTime, config.conf["clockAndCalendar"]["input24HourFormat"]):
			return True
		return False
