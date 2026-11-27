# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.
# Precision timing and BBC pips support by Toby Heath, 2026.

import wave
from datetime import datetime, timedelta
from typing import Dict, Optional

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
	with wave.open(sound, "r") as f:
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
		self._lastAnnouncedBoundary: Optional[datetime] = None

	def terminate(self) -> None:
		self._autoAnnounceClockTimer.Stop()
		del self._autoAnnounceClockTimer

	def _handleClockAnnouncement(self) -> None:
		now = datetime.now()
		autoAnnounce = config.conf["clockAndCalendar"]["autoAnnounce"]
		if autoAnnounce not in autoAnnounceIntervals:
			return

		interval = autoAnnounceIntervals[autoAnnounce]
		boundary = now.replace(second=0, microsecond=0)
		past = now.minute % interval
		# During the first second of a scheduled minute, a late tick still belongs to that minute.
		if past or now.second:
			boundary += timedelta(minutes=interval - past)
		if boundary == self._lastAnnouncedBoundary:
			return

		secs_to_boundary = (boundary - now).total_seconds()
		if secs_to_boundary <= 0.5:
			self._lastAnnouncedBoundary = boundary
			self.reportClock(boundary)
			return

		timeReporting = config.conf["clockAndCalendar"]["timeReporting"]
		is_sound_speech = timeReporting == 0
		is_sound_only = timeReporting == 2

		if is_sound_speech:
			# Precision mode: start the chime early so it finishes on the boundary
			waveFile = self._getWaveFile(boundary)
			sound_name = os.path.basename(waveFile)

			if sound_name == _BBC_PIPS_FILE:
				lead_time = _BBC_PIPS_FINAL_ONSET
			else:
				lead_time = getWaveFileDurationExact(waveFile)

			# Fire when we're within lead_time + 0.5s of the boundary
			if secs_to_boundary <= lead_time + 0.5:
				self._lastAnnouncedBoundary = boundary
				self._reportClockPrecision(waveFile, secs_to_boundary, sound_name)
		elif is_sound_only:
			# Sound-only: only BBC pips needs precision (6th pip on :00).
			waveFile = self._getWaveFile(boundary)
			sound_name = os.path.basename(waveFile)

			if sound_name == _BBC_PIPS_FILE:
				if secs_to_boundary <= _BBC_PIPS_FINAL_ONSET + 0.5:
					self._lastAnnouncedBoundary = boundary
					if not self.quietHoursAreActive():
						nvwave.playWaveFile(waveFile)

	def _getWaveFile(self, boundary: datetime) -> str:
		settings = config.conf["clockAndCalendar"]
		if settings["separateReportSounds"] and boundary.minute != 0:
			return os.path.join(paths.SOUNDS_DIR, settings["timeIntermediateReportSound"])
		return os.path.join(paths.SOUNDS_DIR, settings["timeReportSound"])

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
				None,
				None,
				now,
				formats.rgx.sub(
					formats.repl,
					formats.timeFormats[config.conf["clockAndCalendar"]["timeDisplayFormat"]],
				),
			),
		)

	def reportClock(self, now: Optional[datetime] = None) -> None:
		if now is None:
			now = datetime.now()
		if self.quietHoursAreActive():
			return
		waveFile = self._getWaveFile(now)
		if config.conf["clockAndCalendar"]["timeReporting"] != 1:
			nvwave.playWaveFile(waveFile)
		if config.conf["clockAndCalendar"]["timeReporting"] != 2:
			if config.conf["clockAndCalendar"]["timeReporting"] == 0:
				waveFileDuration = getWaveFileDuration(waveFile)
				wx.CallLater(
					10 + (1000 * waveFileDuration),
					ui.message,
					safeGetTimeFormatEx(
						None,
						None,
						now,
						formats.rgx.sub(
							formats.repl,
							formats.timeFormats[config.conf["clockAndCalendar"]["timeDisplayFormat"]],
						),
					),
				)
			else:
				ui.message(
					safeGetTimeFormatEx(
						None,
						None,
						now,
						formats.rgx.sub(
							formats.repl,
							formats.timeFormats[config.conf["clockAndCalendar"]["timeDisplayFormat"]],
						),
					),
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
			qhStartTime,
			qhEndTime,
			nowTime,
			config.conf["clockAndCalendar"]["input24HourFormat"],
		):
			return True
		return False
