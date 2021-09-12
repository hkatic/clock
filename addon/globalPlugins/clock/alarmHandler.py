# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

import time
import threading
import config
import nvwave

run = False


def runAlarm(sound: str) -> None:
	"""
	A function that allows to launch the scheduled alarm.
	It resets the settings of the alarm launch time after execution.
	@param sound: The path to the WAV file to launch.
	@type sound: basestring.
	"""
	nvwave.playWaveFile(sound)
	config.conf['clockAndCalendar']['alarmTime'] = 0.0
	config.conf['clockAndCalendar']['alarmSavedTime'] = 0.0
	# We save the configuration, in case the user would not have checked the
	# "Save configuration on exit" checkbox in General settings.
	if not config.conf['general']['saveConfigurationOnExit']:
		config.conf.save()


class AlarmTimer(threading.Timer):
	"""
	A subclass of the threading._ Timer class that adds the ability to find the elapsed time
	as well as the remaining time
	"""
	startTiming = None

	def start(self) -> None:
		self.startTiming = time.time()
		# We check whether NVDA has been restarted or not.
		if config.conf['clockAndCalendar']['alarmSavedTime'] == 0.0:
			# NVDA has not been restarted
			config.conf['clockAndCalendar']['alarmSavedTime'] = self.startTiming
		else:
			# NVDA has been restarted.
			self.startTiming = config.conf['clockAndCalendar']['alarmSavedTime']
		threading.Timer.start(self)

	def elapsed(self) -> float:
		return time.time() - self.startTiming if self.is_alive() else 0

	def remaining(self) -> float:
		return config.conf['clockAndCalendar']['alarmTime'] - self.elapsed() if self.is_alive() else 0

	def cancel(self) -> None:
		threading.Timer.cancel(self)
		config.conf['clockAndCalendar']['alarmTime'] = 0.0
		config.conf['clockAndCalendar']['alarmSavedTime'] = 0.0
		# We save the configuration, in case the user would not have checked the
		# "Save configuration on exit" checkbox in General settings.
		if not config.conf['general']['saveConfigurationOnExit']:
			config.conf.save()
