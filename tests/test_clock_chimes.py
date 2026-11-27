import sys
import unittest
from datetime import datetime, timedelta
from importlib import import_module
from pathlib import Path
from types import ModuleType
from unittest.mock import Mock, patch


CLOCK_DIR = Path(__file__).resolve().parents[1] / "addon" / "globalPlugins" / "clock"


class ClockChimeTests(unittest.TestCase):
	def setUp(self):
		# Load the timer without starting NVDA or opening an audio device.
		package = ModuleType("chime_test_plugin")
		package.__path__ = [str(CLOCK_DIR)]
		modules = {
			package.__name__: package,
			f"{package.__name__}.formats": Mock(timeFormats=["HH:mm"]),
			f"{package.__name__}.paths": Mock(SOUNDS_DIR=str(CLOCK_DIR / "waves")),
			**{name: Mock() for name in ("config", "nvwave", "ui", "wx")},
		}
		with patch.dict(sys.modules, modules):
			self.handler = import_module(f"{package.__name__}.clockHandler")
		self.settings = {
			"autoAnnounce": self.handler.AutoAnnounceIntervalEvery15Mins,
			"timeReporting": 2,
			"quietHours": False,
			"separateReportSounds": True,
			"timeReportSound": "bell.wav",
			"timeIntermediateReportSound": "light_bell.wav",
			"timeDisplayFormat": 0,
		}
		self.handler.config.conf = {"clockAndCalendar": self.settings}
		self.handler.datetime = Mock(wraps=datetime)
		self.clock = self.handler.Clock()

	def tick(self, time):
		self.handler.datetime.now.return_value = time
		self.clock._handleClockAnnouncement()

	def assertPlayedOnce(self, filename):
		self.handler.nvwave.playWaveFile.assert_called_once_with(str(CLOCK_DIR / "waves" / filename))

	def test_hourly_chime_from_tick_before_midnight(self):
		midnight = datetime(2026, 12, 1)
		for interval in self.handler.autoAnnounceIntervals:
			with self.subTest(interval=interval):
				self.clock = self.handler.Clock()
				self.settings["autoAnnounce"] = interval
				self.handler.nvwave.playWaveFile.reset_mock()
				self.tick(midnight - timedelta(milliseconds=200))
				self.tick(midnight + timedelta(milliseconds=800))
				self.assertPlayedOnce("bell.wav")

	def test_first_tick_after_hour_still_rings(self):
		self.tick(datetime(2026, 11, 30, 12, 59, 59, 100000))
		self.handler.nvwave.playWaveFile.assert_not_called()
		self.tick(datetime(2026, 11, 30, 13, 0, 0, 100000))
		self.assertPlayedOnce("bell.wav")

	def test_intermediate_chime(self):
		self.tick(datetime(2026, 11, 30, 13, 14, 59, 800000))
		self.tick(datetime(2026, 11, 30, 13, 15, 0, 800000))
		self.assertPlayedOnce("light_bell.wav")
		self.handler.nvwave.playWaveFile.reset_mock()
		self.tick(datetime(2026, 11, 30, 13, 59, 59, 800000))
		self.assertPlayedOnce("bell.wav")

	def test_shared_chime(self):
		self.settings["separateReportSounds"] = False
		self.tick(datetime(2026, 11, 30, 13, 14, 59, 800000))
		self.assertPlayedOnce("bell.wav")

	def test_bbc_pips_start_before_hour_and_only_once(self):
		self.settings["timeReportSound"] = "clock_cuckoo7.wav"
		hour = datetime(2026, 11, 30, 13)
		self.tick(hour - timedelta(seconds=5.2))
		self.assertPlayedOnce("clock_cuckoo7.wav")
		self.tick(hour - timedelta(milliseconds=200))
		self.tick(hour + timedelta(milliseconds=800))
		self.assertPlayedOnce("clock_cuckoo7.wav")

	def test_sound_and_speech_fallback_uses_hour_being_announced(self):
		self.settings["timeReporting"] = 0
		hour = datetime(2026, 11, 30, 13)
		self.tick(hour - timedelta(milliseconds=200))
		self.assertPlayedOnce("bell.wav")
		self.assertEqual(self.handler.safeGetTimeFormatEx.call_args.args[2], hour)
		self.handler.wx.CallLater.assert_called_once()

	def test_sound_and_speech_starts_hourly_chime_in_advance(self):
		self.settings["timeReporting"] = 0
		hour = datetime(2026, 11, 30, 13)
		self.tick(hour - timedelta(seconds=1))
		self.assertPlayedOnce("bell.wav")
		self.handler.wx.CallLater.assert_called_once_with(1000, self.clock._speakCurrentTime)
		self.tick(hour)
		self.assertPlayedOnce("bell.wav")

	def test_speech_only_announces_the_scheduled_time_once(self):
		self.settings["timeReporting"] = 1
		hour = datetime(2026, 11, 30, 13)
		self.tick(hour - timedelta(milliseconds=200))
		self.tick(hour + timedelta(milliseconds=800))
		self.assertEqual(self.handler.safeGetTimeFormatEx.call_args.args[2], hour)
		self.handler.ui.message.assert_called_once()
		self.handler.nvwave.playWaveFile.assert_not_called()
