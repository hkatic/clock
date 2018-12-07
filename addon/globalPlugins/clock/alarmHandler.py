# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

import time
import os
import nvwave
import paths
import threading
import config

run = False

class AlarmTimer (threading._Timer):
	"""
	A subclass of the threading._ Timer class that adds the ability to find the elapsed time as well as the remaining time
	"""
	startTiming = None

	def start (self):
		self.startTiming = time.time ()
		threading._Timer.start (self)

	def elapsed (self):
		return time.time () - self.startTiming if self.is_alive () else 0

	def remaining (self):
		return self.interval - self.elapsed () if self.is_alive () else 0

	def cancel (self):
		threading._Timer.cancel (self)
		config.conf["clockAndCalendar"]["alarm"] = False


