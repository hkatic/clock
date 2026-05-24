# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.
# Precision timing and BBC pips support by Toby Heath, 2026.

import math
import wave
from datetime import datetime, timedelta
from typing import Dict

import config
import nvwave
import os
import ui
import wx

from . import dtfunctions
from . import formats
from . import paths
from .formats import safeGetTimeFormatEx

# BBC pips (clock_cuckoo7.wav): 5 short pips then a 6th long pip marking the hour.
# The final long pip starts at 5.22s into the 5.91s file.
# Speech should fire WITH the 6th pip, not after the file ends.
_BBC_PIPS_FILE = "clock_cuckoo7.wav"
_BBC_PIPS_FINAL_ONSET = 5.22


def getWaveFileDuration(sound: str) -> int:
	"""
	A function for calculating the duration of the wave file to be launched at regular intervals.
	It allows to delay the announcement of the time immediately after the sound is launched.
	@param sound: The path to the WAV file.
	@type sound: basestring.
	@returns: The duration of the wav file in seconds.
	@rtype: int.
	"""
	return int(getWaveFileDurationExact(sound))


def getWaveFileDurationExact(sound: str) -> float:
	"""Return exact WAV duration as float seconds."""
	with wave.open(sound, 'r') as f:
		return f.getnframes() / f.getframerate()


AutoAnnounceIntervalEvery5Mins = 1
AutoAnnounceIntervalEvery10Mins = 2
AutoAnnounceIntervalEvery15Mins = 3
AutoAnnounceIntervalEvery30Mins = 4
AutoAnnounceIntervalEveryHour = 5


autoAnnounceIntervals: Dict[int, int] = {
	AutoAnnounceIntervalEvery5Mins: 5,
	AutoAnnounceIntervalEvery10Mins: 10,

	AutoAnnounceIntervalEvery15Mins: 15,
	AutoAnnounceIntervalEvery30Mins: 30,
	AutoAnnounceIntervalEveryHour: 60,
}


class Clock(object):

	def __init__(self) -> None:
		self._autoAnnounceClockTimer = wx.PyTimer(self._handleClockAnnouncement)
		self._autoAnnounceClockTimer.Start(1000)
		self._announcedThisBoundary = False
		self._lastBoundaryKey = None

	def terminate(self) -> None:
		self._autoAnnounceClockTimer.Stop()
		del self._autoAnnounceClockTimer

	def _handleClockAnnouncement(self) -> None:
		now = datetime.now()
		autoAnnounce = config.conf["clockAndCalendar"]["autoAnnounce"]
		if autoAnnounce not in autoAnnounceIntervals:
			return

		interval = autoAnnounceIntervals[autoAnnounce]
		minute = now.minute
		second = now.second + now.microsecond / 1_000_000

		# Calculate seconds until the next interval boundary
		past = minute % interval
		minutes_until = interval - past
		secs_to_boundary = (minutes_until * 60) - second

		# Identify which boundary we're approaching
		boundary_key = self._getBoundaryKey(now, interval)

		# Reset the guard when we move to a new boundary
		if boundary_key != self._lastBoundaryKey:
			self._announcedThisBoundary = False
			self._lastBoundaryKey = boundary_key

		if self._announcedThisBoundary:
			return

		timeReporting = config.conf["clockAndCalendar"]["timeReporting"]
		is_sound_speech = timeReporting == 0
		is_sound_only = timeReporting == 2

		if is_sound_speech and secs_to_boundary > 0.5:
			# Precision mode: start the chime early so it finishes on the boundary
			waveFile = self._getWaveFile(now, interval)
			sound_name = os.path.basename(waveFile)

			if sound_name == _BBC_PIPS_FILE:
				lead_time = _BBC_PIPS_FINAL_ONSET
			else:
				lead_time = getWaveFileDurationExact(waveFile)

			# Fire when we're within lead_time + 0.5s of the boundary
			if secs_to_boundary <= lead_time + 0.5:
				self._announcedThisBoundary = True
				self._reportClockPrecision(waveFile, secs_to_boundary, sound_name)
		elif is_sound_only and secs_to_boundary > 0.5:
			# Sound-only: only BBC pips needs precision (6th pip on :00).
			# All other sounds just play at :00 via the fallback below.
			waveFile = self._getWaveFile(now, interval)
			sound_name = os.path.basename(waveFile)

			if sound_name == _BBC_PIPS_FILE:
				if secs_to_boundary <= _BBC_PIPS_FINAL_ONSET + 0.5:
					self._announcedThisBoundary = True
					if not self.quietHoursAreActive():
						nvwave.playWaveFile(waveFile)
		elif secs_to_boundary <= 0.5 or (past == 0 and second < 1):
			# Non-precision modes or boundary reached
			self._announcedThisBoundary = True
			self.reportClock()

	def _getBoundaryKey(self, now, interval):
		"""Return a unique key for the upcoming boundary to detect transitions."""
		minute = now.minute
		second = now.second
		past = minute % interval
		minutes_until = interval - past
		target = now + timedelta(minutes=minutes_until, seconds=-second)
		return (target.year, target.month, target.day, target.hour, target.minute)

	def _getWaveFile(self, now, interval):
		"""Get the appropriate wave file for the upcoming boundary."""
		secs_into_hour = now.minute * 60 + now.second
		interval_secs = interval * 60
		target_minute = math.ceil(secs_into_hour / interval_secs) * interval % 60

		if config.conf["clockAndCalendar"]["separateReportSounds"]:
			if target_minute == 0:
				return os.path.join(paths.SOUNDS_DIR, config.conf["clockAndCalendar"]["timeReportSound"])
			else:
				return os.path.join(paths.SOUNDS_DIR, config.conf["clockAndCalendar"]["timeIntermediateReportSound"])
		return os.path.join(paths.SOUNDS_DIR, config.conf["clockAndCalendar"]["timeReportSound"])

	def _getBoundaryTime(self, now, secs_to_boundary):
		"""Calculate the exact datetime of the upcoming boundary."""
		boundary = now + timedelta(seconds=secs_to_boundary)
		return boundary.replace(second=0, microsecond=0)

	def _reportClockPrecision(self, waveFile, secs_to_boundary, sound_name) -> None:
		"""Sound+speech with precision timing: chime finishes at the boundary, then speech."""
		if self.quietHoursAreActive():
			return

		nvwave.playWaveFile(waveFile)

		# For BBC pips the speech should coincide with the final (6th) pip,
		# not the minute boundary.  Use the known onset so timer jitter
		# doesn't push speech ahead of the pip.
		if sound_name == _BBC_PIPS_FILE:
			delay_ms = max(int(_BBC_PIPS_FINAL_ONSET * 1000), 10)
		else:
			delay_ms = max(int(secs_to_boundary * 1000), 10)

		# Defer the time read until speech actually fires, so it
		# announces the real current time at that instant.
		wx.CallLater(delay_ms, self._speakCurrentTime)

	def _speakCurrentTime(self) -> None:
		"""Announce the current time right now (called via CallLater)."""
		now = datetime.now()
		ui.message(
			safeGetTimeFormatEx(
				None, None, now, formats.rgx.sub(
					formats.repl, formats.timeFormats[config.conf['clockAndCalendar']['timeDisplayFormat']]
				)
			)
		)

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
					safeGetTimeFormatEx(
						None, None, now, formats.rgx.sub(
							formats.repl, formats.timeFormats[config.conf['clockAndCalendar']['timeDisplayFormat']]
						)
					)
				)
			else:
				ui.message(
					safeGetTimeFormatEx(
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
