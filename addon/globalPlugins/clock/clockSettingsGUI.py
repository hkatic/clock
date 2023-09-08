# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

import re
import datetime
from . import paths
from . import formats
import config
import nvwave
import gui
import os
import wx
from . import alarmHandler
from . import dtfunctions
from gui import SettingsPanel, SettingsDialog

import addonHandler
addonHandler.initTranslation()


class ClockSettingsPanel(SettingsPanel):

	# Translators: This is the label for the clock settings panel.
	title = _("Clock")

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

		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._autoAnnounce = _("&Interval:")

		self._timeAnnounceChoices = (
			# Translators: This is a choice of the time report choices combo box.
			_("message and sound"),
			# Translators: This is a choice of the time report choices combo box.
			_("message only"),
			# Translators: This is a choice of the time report choices combo box.
			_("sound only")
		)

		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._timeReport = _("Time &announcement:")

		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._timeReportSound = _("Clock chime &sound:")

		# Translators: This is the label for a checkbox in the Clock settings dialog.
		self._separateReportSounds = _("&Separate hour/minute chimes")

		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._timeIntermediateReportSound = _("Interval chime &sound:")

		# Translators: This is the label for a checkbox in the Clock settings dialog.
		self._quietHours = _("&Quiet hours")

		self._quietHourTimeFormatChoices = (
			# Translators: This is a choice of the quiet hours time format choices.
			_("12-hour format"),
			# Translators: This is a choice of the quiet hours time format choices.
			_("24-hour format")
		)

		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._input24HourFormat = _("Quiet hours time &format:")

		self.hoursList12 = [f"{hour} AM" for hour in range(12)]
		self.hoursList12 += [f"{hour} PM" for hour in range(12)]
		self.hoursList12[0], self.hoursList12[12] = "12 AM", "12 PM"
		self.hoursList24 = [str(hour).zfill(2) for hour in range(24)]
		self.minutesList = [str(min).zfill(2) for min in range(60)]

		# Translators: This is the label for an group in the Clock settings dialog.
		self._quietStartTime = _("Quiet hours start time")

		# Translators: This is the label for an group in the Clock settings dialog.
		self._quietEndTime = _("Quiet hours end time")

		self.showSettingsDialog(settingsSizer=settingsSizer)

	def showSettingsDialog(self, settingsSizer):
		clockSettingsGuiHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self._timeDisplayFormatChoice = clockSettingsGuiHelper.addLabeledControl(
			self._timeDisplayFormat, wx.Choice, choices=formats.timeDisplayFormats
		)
		self._dateDisplayFormatChoice = clockSettingsGuiHelper.addLabeledControl(
			self._dateDisplayFormat, wx.Choice, choices=formats.dateDisplayFormats
		)
		self._autoAnnounceChoice = clockSettingsGuiHelper.addLabeledControl(
			self._autoAnnounce, wx.Choice, choices=self._announceChoices
		)
		self._timeReportChoice = clockSettingsGuiHelper.addLabeledControl(
			self._timeReport, wx.Choice, choices=self._timeAnnounceChoices
		)
		self._timeReportSoundChoice = clockSettingsGuiHelper.addLabeledControl(
			self._timeReportSound, wx.Choice, choices=paths.LIST_SOUNDS
		)
		self._separateReportSoundsCheckBox = clockSettingsGuiHelper.addItem(
			wx.CheckBox(self, label=self._separateReportSounds)
		)
		self._timeIntermediateReportSoundChoice = clockSettingsGuiHelper.addLabeledControl(
			self._timeIntermediateReportSound, wx.Choice, choices=paths.LIST_SOUNDS
		)		
		self._quietHoursCheckBox = clockSettingsGuiHelper.addItem(
			wx.CheckBox(self, label=self._quietHours)
		)
		self._input24HourFormatChoice = clockSettingsGuiHelper.addLabeledControl(
			self._input24HourFormat, wx.Choice, choices=self._quietHourTimeFormatChoices
		)
		# Build appropriate hours list with or without period suffix.
		if not config.conf["clockAndCalendar"]["input24HourFormat"]:
			hoursList = self.hoursList12
		else:
			hoursList = self.hoursList24
		self._quietHoursStartGroup = gui.guiHelper.BoxSizerHelper(
			self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=self._quietStartTime), wx.HORIZONTAL)
		)
		clockSettingsGuiHelper.addItem(self._quietHoursStartGroup)
		self.startHourEntry = self._quietHoursStartGroup.addLabeledControl(
			# Translators: the hour label in quiet hours group.
			_("Hour:"), wx.Choice, choices=hoursList
		)
		self.startMinEntry = self._quietHoursStartGroup.addLabeledControl(
			# Translators: the minute label in quiet hours group.
			_("Minute:"), wx.Choice, choices=self.minutesList
		)
		self._quietHoursEndGroup = gui.guiHelper.BoxSizerHelper(
			self, sizer=wx.StaticBoxSizer(wx.StaticBox(self, label=self._quietEndTime), wx.HORIZONTAL)
		)
		clockSettingsGuiHelper.addItem(self._quietHoursEndGroup)
		self.endHourEntry = self._quietHoursEndGroup.addLabeledControl(
			# Translators: the hour label in quiet hours group.
			_("Hour:"), wx.Choice, choices=hoursList
		)
		self.endMinEntry = self._quietHoursEndGroup.addLabeledControl(
			# Translators: the minute label in quiet hours group.
			_("Minute:"), wx.Choice, choices=self.minutesList
		)

		# Event.
		self._timeIntermediateReportSoundChoice.SetStringSelection(config.conf["clockAndCalendar"]["timeIntermediateReportSound"])
		self._timeReportSoundChoice.SetStringSelection(config.conf["clockAndCalendar"]["timeReportSound"])
		self._timeIntermediateReportSoundChoice.Bind(wx.EVT_CHOICE, self.onSoundSelected)
		self._separateReportSoundsCheckBox.Bind(wx.EVT_CHECKBOX, self.onSeparateReportSoundsToggle)
		self._timeReportSoundChoice.Bind(wx.EVT_CHOICE, self.onSoundSelected)
		self._autoAnnounceChoice.Bind(wx.EVT_CHOICE, self.onAutoAnnounce)
		self._quietHoursCheckBox.Bind(wx.EVT_CHECKBOX, self.onQuietHoursToggle)
		self._input24HourFormatChoice.Bind(wx.EVT_CHOICE, self.onInput24HourFormat)
		self.setValues()

	def onAutoAnnounce(self, evt):
		evt.Skip()
		self._timeReportChoice.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._quietHoursCheckBox.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._timeIntermediateReportSoundChoice.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._timeReportSoundChoice.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._separateReportSoundsCheckBox.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._input24HourFormatChoice.Enabled = (
			self._quietHoursCheckBox.IsChecked() and self._quietHoursCheckBox.IsEnabled()
		)
		self.startHourEntry.Enable(self._quietHoursCheckBox.IsChecked() and self._quietHoursCheckBox.IsEnabled())
		self.startMinEntry.Enable(self._quietHoursCheckBox.IsChecked() and self._quietHoursCheckBox.IsEnabled())
		self.endHourEntry.Enable(self._quietHoursCheckBox.IsChecked() and self._quietHoursCheckBox.IsEnabled())
		self.endMinEntry.Enable(self._quietHoursCheckBox.IsChecked() and self._quietHoursCheckBox.IsEnabled())

	def onSoundSelected(self, evt):
		return nvwave.playWaveFile(os.path.join(paths.SOUNDS_DIR, evt.GetString()))

	def onSeparateReportSoundsToggle(self, evt):
		evt.Skip()
		self._timeIntermediateReportSoundChoice.Enabled = self._separateReportSoundsCheckBox.IsChecked()

	def onQuietHoursToggle(self, evt):
		evt.Skip()
		self._input24HourFormatChoice.Enabled = self._quietHoursCheckBox.GetValue()
		self.startHourEntry.Enable(self._quietHoursCheckBox.GetValue())
		self.startMinEntry.Enable(self._quietHoursCheckBox.GetValue())
		self.endHourEntry.Enable(self._quietHoursCheckBox.GetValue())
		self.endMinEntry.Enable(self._quietHoursCheckBox.GetValue())

	def onInput24HourFormat(self, evt):
		evt.Skip()
		startHourSelection = self.startHourEntry.GetSelection()
		endHourSelection = self.endHourEntry.GetSelection()
		if self._input24HourFormatChoice.GetSelection() == 0:
			self.startHourEntry.Set(self.hoursList12)
			self.endHourEntry.Set(self.hoursList12)
		else:
			self.startHourEntry.Set(self.hoursList24)
			self.endHourEntry.Set(self.hoursList24)
		self.startHourEntry.SetSelection(startHourSelection)
		self.endHourEntry.SetSelection(endHourSelection)

	def setValues(self):
		for index, fmt in enumerate(formats.timeFormats):
			if index == config.conf["clockAndCalendar"]["timeDisplayFormat"]:
				self._timeDisplayFormatChoice.SetSelection(index)
				break
		for index, fmt in enumerate(formats.dateFormats):
			if index == config.conf["clockAndCalendar"]["dateDisplayFormat"]:
				self._dateDisplayFormatChoice.SetSelection(index)
				break
		if config.conf["clockAndCalendar"]["quietHoursStartTime"]:
			quietHoursStartTime = dtfunctions.parseTime(
				config.conf["clockAndCalendar"]["quietHoursStartTime"],
				parse24hour=config.conf["clockAndCalendar"]["input24HourFormat"]
			)
		else:
			quietHoursStartTime = datetime.time()
		if config.conf["clockAndCalendar"]["quietHoursEndTime"]:
			quietHoursEndTime = dtfunctions.parseTime(
				config.conf["clockAndCalendar"]["quietHoursEndTime"],
				parse24hour=config.conf["clockAndCalendar"]["input24HourFormat"]
			)
		else:
			quietHoursEndTime = datetime.time()
		self._autoAnnounceChoice.SetSelection(config.conf["clockAndCalendar"]["autoAnnounce"])
		self._timeReportChoice.SetSelection(config.conf["clockAndCalendar"]["timeReporting"])
		self._quietHoursCheckBox.SetValue(config.conf["clockAndCalendar"]["quietHours"])
		self._separateReportSoundsCheckBox.SetValue(config.conf["clockAndCalendar"]["separateReportSounds"])
		self._input24HourFormatChoice.SetSelection(config.conf["clockAndCalendar"]["input24HourFormat"])
		self.startHourEntry.SetSelection(quietHoursStartTime.hour)
		self.startMinEntry.SetSelection(quietHoursStartTime.minute)
		self.endHourEntry.SetSelection(quietHoursEndTime.hour)
		self.endMinEntry.SetSelection(quietHoursEndTime.minute)
		self._timeReportChoice.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._quietHoursCheckBox.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._timeReportSoundChoice.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._timeIntermediateReportSoundChoice.Enabled = bool(self._autoAnnounceChoice.GetSelection() and self._separateReportSoundsCheckBox.IsChecked())
		self._input24HourFormatChoice.Enabled = (
			self._quietHoursCheckBox.IsChecked() and self._quietHoursCheckBox.IsEnabled()
		)
		self.startHourEntry.Enable(self._quietHoursCheckBox.IsChecked() and self._quietHoursCheckBox.IsEnabled())
		self.startMinEntry.Enable(self._quietHoursCheckBox.IsChecked() and self._quietHoursCheckBox.IsEnabled())
		self.endHourEntry.Enable(self._quietHoursCheckBox.IsChecked() and self._quietHoursCheckBox.IsEnabled())
		self.endMinEntry.Enable(self._quietHoursCheckBox.IsChecked() and self._quietHoursCheckBox.IsEnabled())

	def onSave(self):
		config.conf["clockAndCalendar"]["timeDisplayFormat"] = self._timeDisplayFormatChoice.GetSelection()
		config.conf["clockAndCalendar"]["dateDisplayFormat"] = self._dateDisplayFormatChoice.GetSelection()
		config.conf["clockAndCalendar"]["input24HourFormat"] = bool(self._input24HourFormatChoice.GetSelection())
		config.conf["clockAndCalendar"]["autoAnnounce"] = self._autoAnnounceChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeReporting"] = self._timeReportChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeIntermediateReportSound"] = self._timeIntermediateReportSoundChoice.GetStringSelection()
		config.conf["clockAndCalendar"]["separateReportSounds"] = self._separateReportSoundsCheckBox.GetValue()
		config.conf["clockAndCalendar"]["timeReportSound"] = self._timeReportSoundChoice.GetStringSelection()
		quietHours = self._quietHoursCheckBox.GetValue()
		config.conf["clockAndCalendar"]["quietHours"] = quietHours
		quietHoursStartTime = ""
		quietHoursEndTime = ""
		if quietHours:
			startHour = self.startHourEntry.GetSelection()
			startMin = self.startMinEntry.GetSelection()
			endHour = self.endHourEntry.GetSelection()
			endMin = self.endMinEntry.GetSelection()
			if config.conf["clockAndCalendar"]["input24HourFormat"]:
				quietHoursStartTime = f"{startHour:02d}:{startMin:02d}"
				quietHoursEndTime = f"{endHour:02d}:{endMin:02d}"
			else:
				startPeriod, startHour = divmod(startHour, 12)
				startPeriod = "AM" if startPeriod == 0 else "PM"
				if startHour == 0:
					startHour = 12
				quietHoursStartTime = f"{startHour:02d}:{startMin:02d} {startPeriod}"
				endPeriod, endHour = divmod(endHour, 12)
				endPeriod = "AM" if endPeriod == 0 else "PM"
				if endHour == 0:
					endHour = 12
				quietHoursEndTime = f"{endHour:02d}:{endMin:02d} {endPeriod}"
		config.conf["clockAndCalendar"]["quietHoursStartTime"] = quietHoursStartTime
		config.conf["clockAndCalendar"]["quietHoursEndTime"] = quietHoursEndTime


class AlarmSettingsDialog(SettingsDialog):

	# Translators: This is the label for the alarm settings panel.
	title = _("Schedule alarms")
	pause = False

	def makeSettings(self, settingsSizer):
		self._alarmTimerChoices = (
			# Translators: This is an item of the alarm duration choices.
			_("hours"),
			# Translators: This is an item of the alarm duration choices.
			_("minutes"),
			# Translators: This is an item of the alarm duration choices.
			_("seconds")
		)

		# Translators: This is the label for a combo box in the Alarm settings dialog.
		self._alarmTimerTitle = _("&Alarm duration in:")

		# Translators: This is the label for an edit field in the Alarm settings dialog.
		self._alarmTimeWaitingTitle = _("&Duration:")

		# Translators: This is the label for a combo box in the Alarm settings dialog.
		self._alarmSoundTitle = _("A&larm sound:")

		# Translators: This is the label for a button in the Alarm settings dialog.
		self.stopLabel = _("&Stop")

		# Translators: This is the label for a button in the Alarm settings dialog.
		self.pauseLabel = _("&Pause")

		self.showAlarmDialog(settingsSizer=settingsSizer)

	def postInit(self):
		self._alarmTimerChoice.SetFocus()

	def showAlarmDialog(self, settingsSizer):
		alarmSettingsGuiHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self._alarmTimerChoice = alarmSettingsGuiHelper.addLabeledControl(
			self._alarmTimerTitle, wx.Choice, choices=self._alarmTimerChoices
		)
		self._alarmTimeWaitingText = alarmSettingsGuiHelper.addLabeledControl(
			self._alarmTimeWaitingTitle, wx.TextCtrl
		)
		self._alarmSoundChoice = alarmSettingsGuiHelper.addLabeledControl(
			self._alarmSoundTitle, wx.Choice, choices=paths.LIST_ALARMS
		)
		self.stopButton = alarmSettingsGuiHelper.addItem(wx.Button(self, label=self.stopLabel))
		self.pauseButton = alarmSettingsGuiHelper.addItem(wx.Button(self, label=self.pauseLabel))

		# Events.
		self._alarmSoundChoice.Bind(wx.EVT_CHOICE, self.onAlarmSelected)
		self.stopButton.Bind(wx.EVT_BUTTON, self.onStop)
		self.pauseButton.Bind(wx.EVT_BUTTON, self.onPause)

		if config.conf['clockAndCalendar']['alarmSound'] in paths.LIST_ALARMS:
			self._alarmSoundChoice.SetStringSelection(config.conf["clockAndCalendar"]["alarmSound"])
		else:
			self._alarmSoundChoice.SetStringSelection(paths.LIST_ALARMS[0])
		curChoice = config.conf["clockAndCalendar"]["alarmTimerChoice"]
		for index, name in enumerate(self._alarmTimerChoices):
			if index == curChoice:
				self._alarmTimerChoice.SetSelection(index)
				break

	def onStop(self, evt):
		if nvwave.fileWavePlayer is not None:
			nvwave.fileWavePlayer.stop()
			self.pause = False

	def onPause(self, evt):
		if not nvwave.fileWavePlayer:
			return nvwave.playWaveFile(os.path.join(paths.ALARMS_DIR, self._alarmSoundChoice.GetStringSelection()))
		if not nvwave.fileWavePlayer._waveout:
			return nvwave.playWaveFile(os.path.join(paths.ALARMS_DIR, self._alarmSoundChoice.GetStringSelection()))
		self.pause = not self.pause
		return nvwave.fileWavePlayer.pause(self.pause)

	def onAlarmSelected(self, evt):
		self.pause = False
		return nvwave.playWaveFile(os.path.join(paths.ALARMS_DIR, evt.GetString()))

	def onOk(self, evt):
		config.conf["clockAndCalendar"]["alarmSound"] = self._alarmSoundChoice.GetStringSelection()
		config.conf["clockAndCalendar"]["alarmTimerChoice"] = self._alarmTimerChoice.GetSelection()
		self.onStop(None)
		self.postSave()
		super(AlarmSettingsDialog, self).onOk(evt)

	def onCancel(self, evt):
		self.onStop(None)
		super(AlarmSettingsDialog, self).onCancel(evt)

	def postSave(self):
		if re.match(r"\d+", self._alarmTimeWaitingText.GetValue()):
			if gui.messageBox(
				_(
					# Translators: The message displayed after a countdown for an alarm has been chosen.
					"You've chosen an alarm to be triggered in {tm} {unit}"
				).format(tm=self._alarmTimeWaitingText.GetValue(), unit=self._alarmTimerChoice.GetStringSelection()),
				# Translators: The title of the dialog which appears when the user has chosen to trigger an alarm.
				_("Confirmation"), wx.OK | wx.CANCEL | wx.ICON_INFORMATION, self
			) == wx.OK:
				wakeUp = int(self._alarmTimeWaitingText.GetValue())
				if self._alarmTimerChoice.GetSelection() == 0:
					wakeUp *= 3600
				if self._alarmTimerChoice.GetSelection() == 1:
					wakeUp *= 60
				config.conf['clockAndCalendar']['alarmTime'] = wakeUp
				# We save the configuration, in case the user would not have checked the
				# "Save configuration on exit" checkbox in General settings.
				if not config.conf['general']['saveConfigurationOnExit']:
					config.conf.save()
				alarmHandler.run = alarmHandler.AlarmTimer(
					wakeUp, alarmHandler.runAlarm,
					[os.path.join(paths.ALARMS_DIR, self._alarmSoundChoice.GetStringSelection())]
				)
				alarmHandler.run.start()
