# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

from datetime import datetime
import re
import queueHandler
import paths
import api
import formats
import config
import nvwave
import gui
import os
import wx
import locale
import alarmHandler

# This block ensures compatibility with NVDA versions prior to 2018.2 which includes the settings panel.
if hasattr (gui, "SettingsPanel"):
	from gui import SettingsPanel
else:
	from gui.settingsDialogs import SettingsDialog as SettingsPanel

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

		# Translators: This is the label for a checkbox in the Clock settings dialog.
		self._input24HourFormat = _("Input in &24-hour format")

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

		# Translators: This is the label for an edit field in the Clock settings dialog.
		self._quietStartTime = _("Quiet hours start time:")

		# Translators: This is the label for an edit field in the Clock settings dialog.
		self._quietEndTime = _("Quiet hours end time:")

		# This block has been added to ensure the compatibility of the add-on with the NVDA versions that preceded 2016.4, which included the gui.guiHelper module.
		if hasattr (gui, "guiHelper"):
			self.showSettingsDialogForGuiHelper (settingsSizer = settingsSizer)
		else:
			self.showSettingsDialog (settingsSizer = settingsSizer)

	def postInit (self):
		self._timeDisplayFormatChoice.SetFocus ()

	def showSettingsDialogForGuiHelper (self, settingsSizer):
		clockSettingsGuiHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self._timeDisplayFormatChoice = clockSettingsGuiHelper.addLabeledControl(self._timeDisplayFormat, wx.Choice, choices=formats.timeDisplayFormats)
		self._dateDisplayFormatChoice = clockSettingsGuiHelper.addLabeledControl(self._dateDisplayFormat, wx.Choice, choices=formats.dateDisplayFormats)
		self._input24HourFormatCheckBox = clockSettingsGuiHelper.addItem(wx.CheckBox(self, label = self._input24HourFormat))
		self._autoAnnounceChoice = clockSettingsGuiHelper.addLabeledControl(self._autoAnnounce, wx.Choice, choices=self._announceChoices)
		self._timeReportChoice = clockSettingsGuiHelper.addLabeledControl(self._timeReport, wx.Choice, choices=self._timeAnnounceChoices)
		self._timeReportSoundChoice = clockSettingsGuiHelper.addLabeledControl(self._timeReportSound, wx.Choice, choices=paths.LIST_SOUNDS)
		self._quietHoursCheckBox = clockSettingsGuiHelper.addItem(wx.CheckBox(self, label = self._quietHours))
		self._quietStartTimeText = clockSettingsGuiHelper.addLabeledControl(self._quietStartTime, wx.TextCtrl)
		self._quietEndTimeText = clockSettingsGuiHelper.addLabeledControl(self._quietEndTime, wx.TextCtrl)

		# Event.
		self._timeReportSoundChoice.SetStringSelection(config.conf["clockAndCalendar"]["timeReportSound"])
		self._timeReportSoundChoice.Bind(wx.EVT_CHOICE, self.onSoundSelected)
		self._autoAnnounceChoice.Bind(wx.EVT_CHOICE, self.onAutoAnnounce)
		self._quietHoursCheckBox.Bind(wx.EVT_CHECKBOX, self.onQuietHoursToggle)
		self.setValues()

	def showSettingsDialog (self, settingsSizer):
		dialogSizer = wx.BoxSizer (wx.VERTICAL)
		timeFormatLabel = wx.StaticText (self, label = self._timeDisplayFormat)
		dialogSizer.Add (timeFormatLabel)
		self._timeDisplayFormatChoice = wx.Choice (self, choices=formats.timeDisplayFormats)
		dialogSizer.Add (self._timeDisplayFormatChoice)
		dateFormatLabel = wx.StaticText (self, label = self._dateDisplayFormat)
		dialogSizer.Add (dateFormatLabel)
		self._dateDisplayFormatChoice = wx.Choice (self, choices=formats.dateDisplayFormats)
		dialogSizer.Add (self._dateDisplayFormatChoice)
		self._input24HourFormatCheckBox = wx.CheckBox(self, label = self._input24HourFormat)
		dialogSizer.Add (self._input24HourFormatCheckBox)
		autoAnnounceLabel = wx.StaticText (self, label = self._autoAnnounce)
		dialogSizer.Add (autoAnnounceLabel)
		self._autoAnnounceChoice = wx.Choice (self, choices=self._announceChoices)
		dialogSizer.Add (self._autoAnnounceChoice)
		timeReportLabel = wx.StaticText (self, label = self._timeReport)
		dialogSizer.Add (timeReportLabel)
		self._timeReportChoice = wx.Choice (self, choices=self._timeAnnounceChoices)
		dialogSizer.Add (self._timeReportChoice)
		timeSoundLabel = wx.StaticText (self, label = self._timeReportSound)
		dialogSizer.Add (timeSoundLabel)
		self._timeReportSoundChoice = wx.Choice (self, choices=paths.LIST_SOUNDS)
		dialogSizer.Add (self._timeReportSoundChoice)
		self._quietHoursCheckBox = wx.CheckBox(self, label = self._quietHours)
		dialogSizer.Add (self._quietHoursCheckBox)
		startTimeLabel = wx.StaticText (self, label = self._quietStartTime)
		dialogSizer.Add (startTimeLabel)
		self._quietStartTimeText = wx.TextCtrl (self)
		dialogSizer.Add (self._quietStartTimeText)
		endTimeLabel = wx.StaticText (self, label = self._quietEndTime)
		dialogSizer.Add (endTimeLabel)
		self._quietEndTimeText = wx.TextCtrl (self)
		dialogSizer.Add (self._quietEndTimeText)
		settingsSizer.Add (dialogSizer, border=10, flag=wx.BOTTOM)

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
		self._quietStartTimeText.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._quietEndTimeText.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._quietStartTimeText.Enabled = self._quietHoursCheckBox.IsChecked ()
		self._quietEndTimeText.Enabled = self._quietHoursCheckBox.IsChecked ()

	def onSoundSelected(self, evt):
		return nvwave.playWaveFile(os.path.join(paths.SOUNDS_DIR, evt.GetString()))

	def onQuietHoursToggle(self, evt):
		evt.Skip()
		self._quietStartTimeText.Enabled = self._quietHoursCheckBox.GetValue ()
		self._quietEndTimeText.Enabled = self._quietHoursCheckBox.GetValue ()

	def setValues(self):
		for index, (fmt, name) in enumerate (formats.timeFormatsConfig):
			if fmt == config.conf["clockAndCalendar"]["timeDisplayFormat"]:
				self._timeDisplayFormatChoice.SetSelection(index)
				break
		try:
			self._dateDisplayFormatChoice.SetSelection(formats.dateFormats.index(config.conf["clockAndCalendar"]["dateDisplayFormat"]))
		except ValueError:
			pass
		self._input24HourFormatCheckBox.SetValue(config.conf["clockAndCalendar"]["input24HourFormat"])
		self._autoAnnounceChoice.SetSelection(config.conf["clockAndCalendar"]["autoAnnounce"])
		self._timeReportChoice.SetSelection(config.conf["clockAndCalendar"]["timeReporting"])
		self._quietHoursCheckBox.SetValue(config.conf["clockAndCalendar"]["quietHours"])
		self._quietStartTimeText.SetValue(config.conf["clockAndCalendar"]["quietHoursStartTime"])
		self._quietEndTimeText.SetValue(config.conf["clockAndCalendar"]["quietHoursEndTime"])
		self._timeReportChoice.Enabled = bool(self._autoAnnounceChoice.GetSelection())
		self._quietHoursCheckBox.Enabled = bool (self._autoAnnounceChoice.GetSelection())
		self._quietStartTimeText.Enabled = bool (self._autoAnnounceChoice.GetSelection())
		self._quietEndTimeText.Enabled = bool (self._autoAnnounceChoice.GetSelection())
		self._quietStartTimeText.Enabled = self._quietHoursCheckBox.IsChecked ()
		self._quietEndTimeText.Enabled = self._quietHoursCheckBox.IsChecked ()

	def onSave(self):
		config.conf["clockAndCalendar"]["timeDisplayFormat"]=formats.timeFormatsConfig[self._timeDisplayFormatChoice.GetSelection()][0]
		config.conf["clockAndCalendar"]["dateDisplayFormat"]=formats.dateFormats[self._dateDisplayFormatChoice.GetSelection()]
		config.conf["clockAndCalendar"]["input24HourFormat"]=self._input24HourFormatCheckBox.GetValue()
		config.conf["clockAndCalendar"]["autoAnnounce"]=self._autoAnnounceChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeReporting"]=self._timeReportChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeReportSound"]=self._timeReportSoundChoice.GetStringSelection()
		config.conf["clockAndCalendar"]["quietHours"]=self._quietHoursCheckBox.GetValue()
		config.conf["clockAndCalendar"]["quietHoursStartTime"]=self._quietStartTimeText.GetValue()
		config.conf["clockAndCalendar"]["quietHoursEndTime"]=self._quietEndTimeText.GetValue()

	def onOk (self, evt):
		config.conf["clockAndCalendar"]["timeDisplayFormat"]=formats.timeFormatsConfig[self._timeDisplayFormatChoice.GetSelection()][0]
		config.conf["clockAndCalendar"]["dateDisplayFormat"]=formats.dateFormats[self._dateDisplayFormatChoice.GetSelection()]
		config.conf["clockAndCalendar"]["input24HourFormat"]=self._input24HourFormatCheckBox.GetValue()
		config.conf["clockAndCalendar"]["autoAnnounce"]=self._autoAnnounceChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeReporting"]=self._timeReportChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeReportSound"]=self._timeReportSoundChoice.GetStringSelection()
		config.conf["clockAndCalendar"]["quietHours"]=self._quietHoursCheckBox.GetValue()
		config.conf["clockAndCalendar"]["quietHoursStartTime"]=self._quietStartTimeText.GetValue()
		config.conf["clockAndCalendar"]["quietHoursEndTime"]=self._quietEndTimeText.GetValue()
		super(ClockSettingsPanel, self).onOk (evt)

class AlarmSettings (SettingsPanel):

	# Translators: This is the label for the alarm settings dialog.
	title = _("Alarm setup")

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
		self._alarmTimerTitle = _("Choose the type of timer inputs before the alarm rings:")

		# Translators: This is the label for a combo box in the Alarm settings dialog.
		self._alarmSoundTitle = _("A&larm sound:")

		# Translators: This is the label for an edit field in the Alarm settings dialog.
		self._alarmTimeWaitingTitle = _("Alarm time waiting:")

		# This block has been added to ensure the compatibility of the add-on with the NVDA versions that preceded 2016.4, which included the gui.guiHelper module.
		if hasattr (gui, "guiHelper"):
			self.showAlarmDialogForGuiHelper (settingsSizer = settingsSizer)
		else:
			self.showAlarmDialog (settingsSizer = settingsSizer)

	def postInit (self):
				self._alarmTimerChoice.SetFocus ()

	def showAlarmDialogForGuiHelper (self, settingsSizer):
		alarmSettingsGuiHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		self._alarmTimerChoice = alarmSettingsGuiHelper.addLabeledControl(self._alarmTimerTitle, wx.Choice, choices=self._alarmTimerChoices)
		self._alarmTimeWaitingText = alarmSettingsGuiHelper.addLabeledControl(self._alarmTimeWaitingTitle , wx.TextCtrl)
		self._alarmSoundChoice = alarmSettingsGuiHelper.addLabeledControl(self._alarmSoundTitle, wx.Choice, choices=paths.LIST_ALARMS)

		# Events.
		self._alarmSoundChoice.Bind(wx.EVT_CHOICE, self.onAlarmSelected)

		self._alarmSoundChoice.SetStringSelection(config.conf["clockAndCalendar"]["alarmSound"])
		#self._alarmTimeWaitingText.SetValue(config.conf["clockAndCalendar"]["alarmTime"])
		curChoice = config.conf["clockAndCalendar"]["alarmTimerChoice"]
		for index, name in enumerate (self._alarmTimerChoices):
			if index == curChoice:
				self._alarmTimerChoice.SetSelection (index)
				break

	def showAlarmDialog (self, settingsSizer):
		dialogSizer = wx.BoxSizer (wx.VERTICAL)
		labelAlarmTimerChoices = wx.StaticText (self, label = self._alarmTimerTitle)
		dialogSizer.Add (labelAlarmTimerChoices)
		self._alarmTimerChoice = wx.Choice (self, choices=self._alarmTimerChoices)
		dialogSizer.Add (self._alarmTimerChoice)
		labelAlarmTimeWaiting = wx.StaticText (self, label = self._alarmTimeWaitingTitle)
		dialogSizer.Add (labelAlarmTimeWaiting)
		self._alarmTimeWaitingText = wx.TextCtrl (self)
		dialogSizer.Add (self._alarmTimeWaitingText)
		labelAlarmSoundChoices = wx.StaticText (self, label = self._alarmSoundTitle)
		dialogSizer.Add (labelAlarmSoundChoices)
		self._alarmSoundChoice = wx.Choice (self, choices=paths.LIST_ALARMS)
		dialogSizer.Add (self._alarmSoundChoice)

		# Events.
		self._alarmSoundChoice.Bind(wx.EVT_CHOICE, self.onAlarmSelected)

		self._alarmSoundChoice.SetStringSelection(config.conf["clockAndCalendar"]["alarmSound"])
		#self._alarmTimeWaitingText.SetValue(config.conf["clockAndCalendar"]["alarmTime"])
		curChoice = config.conf["clockAndCalendar"]["alarmTimerChoice"]
		for index, name in enumerate (self._alarmTimerChoices):
			if index == curChoice:
				self._alarmTimerChoice.SetSelection (index)
				break

		settingsSizer.Add (dialogSizer, border=10, flag=wx.BOTTOM)

	def onAlarmSelected(self, evt):
		return nvwave.playWaveFile(os.path.join(paths.ALARMS_DIR, evt.GetString()))

	def onOk (self, evt):
		config.conf["clockAndCalendar"]["alarmSound"] = self._alarmSoundChoice.GetStringSelection()
		config.conf["clockAndCalendar"]["alarmTimerChoice"] = self._alarmTimerChoice.GetSelection ()
		config.conf["clockAndCalendar"]["alarmTime"] = self._alarmTimeWaitingText.GetValue()
		self.postSave ()
		super (AlarmSettings, self).onOk (evt)

	def onSave (self):
		config.conf["clockAndCalendar"]["alarmSound"] = self._alarmSoundChoice.GetStringSelection()
		config.conf["clockAndCalendar"]["alarmTimerChoice"] = self._alarmTimerChoice.GetSelection ()
		config.conf["clockAndCalendar"]["alarmTime"] = self._alarmTimeWaitingText.GetValue()

	def postSave (self):
		if re.match (r"\d+", self._alarmTimeWaitingText.GetValue()):
			if gui.messageBox(
				# Translators: The message displayed after a countdown for an alarm has been chosen.
				_(u"You've chosen an alarm to be triggered in {tm} {unit}").format (tm = self._alarmTimeWaitingText.GetValue(), unit = self._alarmTimerChoice.GetStringSelection()),
				# Translators: The title of the dialog which appears when the user has chosen to trigger an alarm.
				_("Confirmation"),wx.OK|wx.CANCEL|wx.ICON_WARNING,self
			)==wx.OK:
				wakeUp = int (self._alarmTimeWaitingText.GetValue ())
				if self._alarmTimerChoice.GetSelection() == 0:
					wakeUp *= 3600
				if self._alarmTimerChoice.GetSelection() == 1:
					wakeUp *= 60
				alarmHandler.run = alarmHandler.AlarmTimer (wakeUp, nvwave.playWaveFile, [os.path.join (paths.ALARMS_DIR, self._alarmSoundChoice.GetStringSelection())])
				alarmHandler.run.start ()
