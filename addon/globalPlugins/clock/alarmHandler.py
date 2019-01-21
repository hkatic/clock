# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

import time
import threading
import config
import nvwave
import sys

TimerBaseClass = threading._Timer if sys.version_info.major == 2 else threading.Timer

run = False

def runAlarm (sound):
	"""
	A function that allows to launch the scheduled alarm.
	It resets the settings of the alarm launch time after execution.
	@param sound: The path to the WAV file to launch.
	@type sound: basestring.
	"""
	nvwave.playWaveFile (sound)
	config.conf['clockAndCalendar']['alarmTime'] = 0.0
	config.conf['clockAndCalendar']['alarmSavedTime'] = 0.0
	config.conf.save ()

class AlarmTimer (TimerBaseClass):
	"""
	A subclass of the threading._ Timer class that adds the ability to find the elapsed time as well as the remaining time
	"""
	startTiming = None

	def start (self):
		self.startTiming = time.time ()
		# We check whether NVDA has been restarted or not.
		if config.conf['clockAndCalendar']['alarmSavedTime'] == 0.0:
			# NVDA has not been restarted
			config.conf['clockAndCalendar']['alarmSavedTime'] = self.startTiming
		else:
			# NVDA has been restarted.
			self.startTiming = config.conf['clockAndCalendar']['alarmSavedTime']
		TimerBaseClass.start (self)

	def elapsed (self):
		return time.time () - self.startTiming if self.is_alive () else 0

	def remaining (self):
		return config.conf['clockAndCalendar']['alarmTime'] - self.elapsed () if self.is_alive () else 0

	def cancel (self):
		TimerBaseClass.cancel (self)
		config.conf['clockAndCalendar']['alarmTime'] = 0.0
		config.conf['clockAndCalendar']['alarmSavedTime'] = 0.0
		config.conf.save ()
