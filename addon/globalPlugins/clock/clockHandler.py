# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

from typing import Dict
from datetime import datetime
from . import dtfunctions
from . import paths
import config
import nvwave
import ui
import os
import wx
from . import formats
from winKernel import GetTimeFormatEx


# A function for getting wav file duration (inspired from this topic:
# https://emiliomm.com/index.php/2016/09/24/getting-duration-of-audio-file-in-python/).
def getWaveFileDuration(sound: str) -> int:
	"""
	A function for calculating the duration of the wave file to be launched at regular intervals.
	It allows to delay the announcement of the time immediately after the sound is launched.
	@param sound: The path to the WAV file.
	@type sound: basestring.
	@returns: The duration of the wav file in seconds.
	@rtype: int.
	"""
	import wave
	with wave.open(sound, 'r') as f:
		frames = f.getnframes()
		rate = f.getframerate()
		duration = frames / rate
	return int(duration)


AutoAnnounceIntervalEvery10Mins = 1
AutoAnnounceIntervalEvery15Mins = 2
AutoAnnounceIntervalEvery30Mins = 3
AutoAnnounceIntervalEveryHour = 4


autoAnnounceIntervals: Dict[int, int] = {
	AutoAnnounceIntervalEvery10Mins: 10,
	AutoAnnounceIntervalEvery15Mins: 15,
	AutoAnnounceIntervalEvery30Mins: 30,
	AutoAnnounceIntervalEveryHour: 60,
}


class Clock(object):

	def __init__(self) -> None:
		self._autoAnnounceClockTimer = wx.PyTimer(self._handleClockAnnouncement)
		self._autoAnnounceClockTimer.Start(1000)

	def terminate(self) -> None:
		self._autoAnnounceClockTimer.Stop()
		del self._autoAnnounceClockTimer

	def _handleClockAnnouncement(self) -> None:
		now = datetime.now()
		if now.second != 0:
			return
		autoAnnounce = config.conf["clockAndCalendar"]["autoAnnounce"]
		if autoAnnounce not in autoAnnounceIntervals:
			return
		if divmod(now.minute, autoAnnounceIntervals[autoAnnounce])[1] == 0:
			self.reportClock()

	def reportClock(self) -> None:
		now = datetime.now()
		if self.quietHoursAreActive():
			return
		if config.conf["clockAndCalendar"]["separateReportSounds"] == True:
				if now.minute == 0:
					waveFile = os.path.join(paths.SOUNDS_DIR, config.conf["clockAndCalendar"]["timeReportSound"])
				else:
					waveFile = os.path.join(paths.SOUNDS_DIR, config.conf["clockAndCalendar"]["timeIntermediateReportSound"])
		else:
			waveFile = os.path.join(paths.SOUNDS_DIR, config.conf["clockAndCalendar"]["timeReportSound"])
		if config.conf["clockAndCalendar"]["timeReporting"] != 1:
			nvwave.playWaveFile(waveFile)
		if config.conf["clockAndCalendar"]["timeReporting"] != 2:
			if config.conf["clockAndCalendar"]["timeReporting"] == 0:
				waveFileDuration = getWaveFileDuration(waveFile)
				wx.CallLater(
					10 + (1000 * waveFileDuration),
					ui.message,
					GetTimeFormatEx(
						None, None, now, formats.rgx.sub(
							formats.repl, formats.timeFormats[config.conf['clockAndCalendar']['timeDisplayFormat']]
						)
					)
				)
			else:
				ui.message(
					GetTimeFormatEx(
						None, None, now, formats.rgx.sub(
							formats.repl, formats.timeFormats[config.conf['clockAndCalendar']['timeDisplayFormat']]
						)
					)
				)

	def quietHoursAreActive(self) -> bool:
		if not config.conf["clockAndCalendar"]["quietHours"]:
			return False
		qhStartTime = config.conf["clockAndCalendar"]["quietHoursStartTime"]
		qhEndTime = config.conf["clockAndCalendar"]["quietHoursEndTime"]
		if not qhStartTime or not qhEndTime:
			return False
		nowTime = dtfunctions.strfNowTime(config.conf["clockAndCalendar"]["input24HourFormat"])
		if dtfunctions.timeInRange(
			qhStartTime, qhEndTime, nowTime, config.conf["clockAndCalendar"]["input24HourFormat"]
		):
			return True
		return False
