# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

from datetime import datetime
import re
import queueHandler
from . import paths
import api
from . import formats
import config
import nvwave
import gui
import os
import wx
import locale
from . import alarmHandler

from gui import SettingsPanel

import addonHandler
addonHandler.initTranslation()

class ClockSettingsPanel(SettingsPanel):

	# Translators: This is the label for the clock settings panel.
	title = _("Clock setup")

	def makeSettings(self, settingsSizer):
		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._timeDisplayFormat = _("&Time display format:")

		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._dateDisplayFormat = _("&Date display format:")

		self._announceChoices = (
			# Translators: This is a choice of the auto announce choices combo box.
			_("off"),
			# Translators: This is a choice of the auto announce choices combo box.
			_("every 10 minutes"),
			# Translators: This is a choice of the auto announce choices combo box.
			_("every 15 minutes"),
			# Translators: This is a choice of the auto announce choices combo box.
			_("every 30 minutes"),
			# Translators: This is a choice of the auto announce choices combo box.
			_("every hour")
		)

		# Transla	tors: This is the label for a combo box in the Clock settings dialog.
		self._autoAnnounce = _("&interval:")

		self._timeAnnounceChoices=(
			# Translators: This is a choice of the time report choices combo box.
			_("speech and sound"),
			# Translators: This is a choice of the time report choices combo box.
			_("speech only"),
			# Translators: This is a choice of the time report choices combo box.
			_("sound only")
		)

		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._timeReport = _("Time &announcement:")

		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._timeReportSound = _("Clock chime &sound:")

		# Translators: This is the label for a checkbox in the Clock settings dialog.
		self._quietHours = _("&Quiet hours")

		# Translators: This is the label for a checkbox in the Clock settings dialog.
		self._input24HourFormat = _("Input in &24-hour format")

		# Translators: This is the label for an edit field in the Clock settings dialog.
		self._quietStartTime = _("Quiet hours start time:")

		# Translators: This is the label for an edit field in the Clock settings dialog.
		self._quietEndTime = _("Quiet hours end time:")

		self.showSettingsDialog (settingsSizer = settingsSizer)

	def showSettingsDialog (self, settingsSizer):
		clockSettingsGuiHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self._timeDisplayFormatChoice = clockSettingsGuiHelper.addLabeledControl(self._timeDisplayFormat, wx.Choice, choices=formats.timeDisplayFormats)
		self._dateDisplayFormatChoice = clockSettingsGuiHelper.addLabeledControl(self._dateDisplayFormat, wx.Choice, choices=formats.dateDisplayFormats)
		self._autoAnnounceChoice = clockSettingsGuiHelper.addLabeledControl(self._autoAnnounce, wx.Choice, choices=self._announceChoices)
		self._timeReportChoice = clockSettingsGuiHelper.addLabeledControl(self._timeReport, wx.Choice, choices=self._timeAnnounceChoices)
		self._timeReportSoundChoice = clockSettingsGuiHelper.addLabeledControl(self._timeReportSound, wx.Choice, choices=paths.LIST_SOUNDS)
		self._quietHoursCheckBox = clockSettingsGuiHelper.addItem(wx.CheckBox(self, label = self._quietHours))
		self._input24HourFormatCheckBox = clockSettingsGuiHelper.addItem(wx.CheckBox(self, label = self._input24HourFormat))
		self._quietStartTimeText = clockSettingsGuiHelper.addLabeledControl(self._quietStartTime, wx.TextCtrl)
		self._quietEndTimeText = clockSettingsGuiHelper.addLabeledControl(self._quietEndTime, wx.TextCtrl)

		# Event.
		self._timeReportSoundChoice.SetStringSelection(config.conf["clockAndCalendar"]["timeReportSound"])
		self._timeReportSoundChoice.Bind(wx.EVT_CHOICE, self.onSoundSelected)
		self._autoAnnounceChoice.Bind(wx.EVT_CHOICE, self.onAutoAnnounce)
		self._quietHoursCheckBox.Bind(wx.EVT_CHECKBOX, self.onQuietHoursToggle)
		self.setValues()

	def onAutoAnnounce(self, evt):
		evt.Skip()
		self._timeReportChoice.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._quietHoursCheckBox.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._timeReportSoundChoice.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._input24HourFormatCheckBox.Enabled = (self._quietHoursCheckBox.IsChecked () and self._quietHoursCheckBox.IsEnabled ())
		self._quietStartTimeText.Enabled = (self._quietHoursCheckBox.IsChecked () and self._quietHoursCheckBox.IsEnabled ())
		self._quietEndTimeText.Enabled = (self._quietHoursCheckBox.IsChecked () and self._quietHoursCheckBox.IsEnabled ())

	def onSoundSelected(self, evt):
		return nvwave.playWaveFile(os.path.join(paths.SOUNDS_DIR, evt.GetString()))

	def onQuietHoursToggle(self, evt):
		evt.Skip()
		self._input24HourFormatCheckBox.Enabled = self._quietHoursCheckBox.GetValue ()
		self._quietStartTimeText.Enabled = self._quietHoursCheckBox.GetValue ()
		self._quietEndTimeText.Enabled = self._quietHoursCheckBox.GetValue ()

	def setValues(self):
		for index, (fmt) in enumerate (formats.timeFormats):
			if index == config.conf["clockAndCalendar"]["timeDisplayFormat"]:
				self._timeDisplayFormatChoice.SetSelection(index)
				break
		for index, (fmt) in enumerate (formats.dateFormats):
			if index == config.conf["clockAndCalendar"]["dateDisplayFormat"]:
				self._dateDisplayFormatChoice.SetSelection(index)
				break
		self._input24HourFormatCheckBox.SetValue(config.conf["clockAndCalendar"]["input24HourFormat"])
		self._autoAnnounceChoice.SetSelection(config.conf["clockAndCalendar"]["autoAnnounce"])
		self._timeReportChoice.SetSelection(config.conf["clockAndCalendar"]["timeReporting"])
		self._quietHoursCheckBox.SetValue(config.conf["clockAndCalendar"]["quietHours"])
		self._quietStartTimeText.SetValue(config.conf["clockAndCalendar"]["quietHoursStartTime"])
		self._quietEndTimeText.SetValue(config.conf["clockAndCalendar"]["quietHoursEndTime"])
		self._timeReportChoice.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._quietHoursCheckBox.Enabled = bool (self._autoAnnounceChoice.GetSelection())
		self._timeReportSoundChoice.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._input24HourFormatCheckBox.Enabled = (self._quietHoursCheckBox.IsChecked () and self._quietHoursCheckBox.IsEnabled ())
		self._quietStartTimeText.Enabled = (self._quietHoursCheckBox.IsChecked () and self._quietHoursCheckBox.IsEnabled ())
		self._quietEndTimeText.Enabled = (self._quietHoursCheckBox.IsChecked () and self._quietHoursCheckBox.IsEnabled ())

	def onSave(self):
		config.conf["clockAndCalendar"]["timeDisplayFormat"]=self._timeDisplayFormatChoice.GetSelection()
		config.conf["clockAndCalendar"]["dateDisplayFormat"]=self._dateDisplayFormatChoice.GetSelection()
		config.conf["clockAndCalendar"]["dateDisplayFormat"]=self._dateDisplayFormatChoice.GetSelection()
		config.conf["clockAndCalendar"]["input24HourFormat"]=self._input24HourFormatCheckBox.GetValue()
		config.conf["clockAndCalendar"]["autoAnnounce"]=self._autoAnnounceChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeReporting"]=self._timeReportChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeReportSound"]=self._timeReportSoundChoice.GetStringSelection()

	def postSave (self):
		match = None
		match1 = None
		if self._quietHoursCheckBox.IsEnabled () and self._quietHoursCheckBox.IsChecked ():
			if self._input24HourFormatCheckBox.IsChecked ():
				match = re.match("^(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$", self._quietStartTimeText.GetValue())
				match1 = re.match("^(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$", self._quietEndTimeText.GetValue())
			else:
				match = re.match("^(0?[0-9]|1[0-2]):[0-5][0-9] [aPAp][mM]$", self._quietStartTimeText.GetValue ())
				match1 = re.match("^(0?[0-9]|1[0-2]):[0-5][0-9] [aPAp][mM]$", self._quietEndTimeText.GetValue ())
			if match and match1:
				config.conf["clockAndCalendar"]["quietHours"]=self._quietHoursCheckBox.GetValue()
				config.conf["clockAndCalendar"]["quietHoursStartTime"]=self._quietStartTimeText.GetValue()
				config.conf["clockAndCalendar"]["quietHoursEndTime"]=self._quietEndTimeText.GetValue()
			else:
				if gui.messageBox(
					# A message that appears to inform the user that he has entered a mistaken value for the quiet hours.
					_(u"The value you entered for your quiet hours is erroneous, for a 24-hour format, the value must be HH:MM, for a 12-hour format, the value must be HH:MM followed by the AM or PM suffix, please reread the documentation. So your quiet hours have been deactivated for prevent any error in the configuration file."),
					# Translators: The title of the dialog which appears when the user has chosen a mistaken value for his quiet hours.
					_("Error"),wx.OK|wx.ICON_ERROR,self
				)==wx.OK:
					config.conf['clockAndCalendar']['quietHours'] = False
		else:
			config.conf['clockAndCalendar']['quietHours'] = False
		# We save the configuration, in case the user would not have checked the "Save configuration on exit" checkbox in General settings.
		if not config.conf['general']['saveConfigurationOnExit']:
			config.conf.save ()

class AlarmSettingsPanel (SettingsPanel):

	# Translators: This is the label for the alarm settings panel.
	title = _("Alarm setup")
	pause = False

	def makeSettings(self, settingsSizer):
		self._alarmTimerChoices=(
			# Translators: This is an item of the alarm timer choices.
			_("Hours"),
			# Translators: This is an item of the alarm timer choices.
			_("Minutes"),
			# Translators: This is an item of the alarm timer choices.
			_("Seconds")
		)

		# Translators: This is the label for a combo box in the Alarm settings dialog.
		self._alarmTimerTitle = _("Choose the type of timer &inputs before the alarm rings:")

		# Translators: This is the label for a combo box in the Alarm settings dialog.
		self._alarmSoundTitle = _("A&larm sound:")

		# Translators: This is the label for a button in the Alarm settings dialog.
		self.stopLabel = _("&Stop")

		# Translators: This is the label for a button in the Alarm settings dialog.
		self.pauseLabel = _("&Pause")

		# Translators: This is the label for an edit field in the Alarm settings dialog.
		self._alarmTimeWaitingTitle = _("Alarm &time waiting:")

		self.showAlarmDialog (settingsSizer = settingsSizer)

	def showAlarmDialog (self, settingsSizer):
		alarmSettingsGuiHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self._alarmTimerChoice = alarmSettingsGuiHelper.addLabeledControl(self._alarmTimerTitle, wx.Choice, choices=self._alarmTimerChoices)
		self._alarmTimeWaitingText = alarmSettingsGuiHelper.addLabeledControl(self._alarmTimeWaitingTitle , wx.TextCtrl)
		self._alarmSoundChoice = alarmSettingsGuiHelper.addLabeledControl(self._alarmSoundTitle, wx.Choice, choices=paths.LIST_ALARMS)
		self.stopButton = alarmSettingsGuiHelper.addItem (wx.Button (self, label = self.stopLabel))
		self.pauseButton = alarmSettingsGuiHelper.addItem (wx.Button (self, label = self.pauseLabel))

		# Events.
		self._alarmSoundChoice.Bind(wx.EVT_CHOICE, self.onAlarmSelected)
		self.stopButton.Bind (wx.EVT_BUTTON, self.onStop )
		self.pauseButton.Bind (wx.EVT_BUTTON, self.onPause )

		if config.conf['clockAndCalendar']['alarmSound'] in paths.LIST_ALARMS:
			self._alarmSoundChoice.SetStringSelection(config.conf["clockAndCalendar"]["alarmSound"])
		else:
			self._alarmSoundChoice.SetStringSelection(paths.LIST_ALARMS[0])
		curChoice = config.conf["clockAndCalendar"]["alarmTimerChoice"]
		for index, name in enumerate (self._alarmTimerChoices):
			if index == curChoice:
				self._alarmTimerChoice.SetSelection (index)
				break

	def onStop (self, evt):
		if nvwave.fileWavePlayer is not None:
			nvwave.fileWavePlayer.stop()
			self.pause = False

	def onPause (self, evt):
		if not nvwave.fileWavePlayer:
			return nvwave.playWaveFile(os.path.join(paths.ALARMS_DIR, self._alarmSoundChoice.GetStringSelection()))
		if not nvwave.fileWavePlayer._waveout:
			return nvwave.playWaveFile(os.path.join(paths.ALARMS_DIR, self._alarmSoundChoice.GetStringSelection()))
		self.pause = not self.pause
		return nvwave.fileWavePlayer.pause(self.pause)

	def onAlarmSelected(self, evt):
		self.pause = False
		return nvwave.playWaveFile(os.path.join(paths.ALARMS_DIR, evt.GetString()))

	def onSave (self):
		config.conf["clockAndCalendar"]["alarmSound"] = self._alarmSoundChoice.GetStringSelection()
		config.conf["clockAndCalendar"]["alarmTimerChoice"] = self._alarmTimerChoice.GetSelection ()

	def postSave (self):
		if re.match (r"\d+", self._alarmTimeWaitingText.GetValue()):
			if gui.messageBox(
				# Translators: The message displayed after a countdown for an alarm has been chosen.
				_(u"You've chosen an alarm to be triggered in {tm} {unit}").format (tm = self._alarmTimeWaitingText.GetValue(), unit = self._alarmTimerChoice.GetStringSelection()),
				# Translators: The title of the dialog which appears when the user has chosen to trigger an alarm.
				_("Confirmation"),wx.OK|wx.CANCEL|wx.ICON_INFORMATION,self
			)==wx.OK:
				wakeUp = int (self._alarmTimeWaitingText.GetValue ())
				if self._alarmTimerChoice.GetSelection() == 0:
					wakeUp *= 3600
				if self._alarmTimerChoice.GetSelection() == 1:
					wakeUp *= 60
				config.conf['clockAndCalendar']['alarmTime'] = wakeUp
				# We save the configuration, in case the user would not have checked the "Save configuration on exit" checkbox in General settings.
				if not config.conf['general']['saveConfigurationOnExit']:
					config.conf.save ()
				alarmHandler.run = alarmHandler.AlarmTimer (wakeUp, alarmHandler.runAlarm, [os.path.join (paths.ALARMS_DIR, self._alarmSoundChoice.GetStringSelection())])
				alarmHandler.run.start ()
