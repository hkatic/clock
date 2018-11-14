# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

from datetime import datetime
import paths
import formats
import config
import nvwave
import gui
import os
import wx
import addonHandler
addonHandler.initTranslation()
import locale

class ClockSettingsPanel(gui.SettingsPanel):
	# Translators: This is the label for the clock settings panel.
	title = _("Clock")

	def makeSettings(self, settingsSizer):
		clockSettingsGuiHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._timeDisplayFormatChoice = clockSettingsGuiHelper.addLabeledControl(_("&Time display format:"), wx.Choice, choices=formats.timeDisplayFormats)
		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._dateDisplayFormatChoice = clockSettingsGuiHelper.addLabeledControl(_("&Date display format:"), wx.Choice, choices=formats.dateDisplayFormats)
		# Translators: This is the label for a checkbox in the Clock settings dialog.
		self.input24HourFormatCheckBox = clockSettingsGuiHelper.addItem(wx.CheckBox(self, label=_("Input in &24-hour format")))
		autoAnnounceChoices=(_("off"), _("every 10 minutes"), _("every 15 minutes"), _("every 30 minutes"), _("every hour"))
		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._autoAnnounceChoice = clockSettingsGuiHelper.addLabeledControl(_("Auto announce &interval:"), wx.Choice, choices=autoAnnounceChoices)
		self._autoAnnounceChoice.Bind(wx.EVT_CHOICE, self.onAutoAnnounce)
		timeReportChoices=(_("speech and sound"), _("speech only"), _("sound only"))
		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._timeReportChoice = clockSettingsGuiHelper.addLabeledControl(_("Time &announcement:"), wx.Choice, choices=timeReportChoices)
		# Translators: This is the label for a combo box in the Clock settings dialog.
		self._timeReportSoundChoice = clockSettingsGuiHelper.addLabeledControl(_("Clock chime &sound:"), wx.Choice, choices=paths.LIST_SOUNDS)
		self._timeReportSoundChoice.SetStringSelection(config.conf["clockAndCalendar"]["timeReportSound"])
		self._timeReportSoundChoice.Bind(wx.EVT_CHOICE, self.onSoundSelected)
		# Translators: This is the label for a checkbox in the Clock settings dialog.
		self.quietHoursCheckBox = clockSettingsGuiHelper.addItem(wx.CheckBox(self, label=_("&Quiet hours")))
		self.quietHoursCheckBox.Bind(wx.EVT_CHECKBOX, self.onQuietHoursToggle)
		# Translators: This is the label for an edit field in the Clock settings dialog.
		self.quietStartTimeText = clockSettingsGuiHelper.addLabeledControl(_("Quiet hours start time:"), wx.TextCtrl)
		# Translators: This is the label for an edit field in the Clock settings dialog.
		self.quietEndTimeText = clockSettingsGuiHelper.addLabeledControl(_("Quiet hours end time:"), wx.TextCtrl)
		self.setValues()

	def onAutoAnnounce(self, evt):
		evt.Skip()
		self.checkAutoAnnounceSetup()
		self.checkQuietHoursSetup()

	def onSoundSelected(self, evt):
		return nvwave.playWaveFile(os.path.join(paths.SOUNDS_DIR, evt.GetString()))

	def onQuietHoursToggle(self, evt):
		evt.Skip()
		self.checkAutoAnnounceSetup()
		self.checkQuietHoursSetup()

	def checkAutoAnnounceSetup(self):
		if self._autoAnnounceChoice.GetSelection()==0:
			self.quietHoursCheckBox.Show(False)
			self.quietStartTimeText.Show(False)
			self.quietEndTimeText.Show(False)
		else:
			self.quietHoursCheckBox.Show(True)
			self.quietStartTimeText.Show(True)
			self.quietEndTimeText.Show(True)

	def checkQuietHoursSetup(self):
		if self.quietHoursCheckBox.GetValue() and self._autoAnnounceChoice.GetSelection()!=0:
			self.quietStartTimeText.Show(True)
			self.quietEndTimeText.Show(True)
		elif not self.quietHoursCheckBox.GetValue():
			self.quietStartTimeText.Show(False)
			self.quietEndTimeText.Show(False)

	def setValues(self):
		try:
			self._timeDisplayFormatChoice.SetSelection(formats.timeFormats.index(config.conf["clockAndCalendar"]["timeDisplayFormat"]))
		except ValueError:
			pass
		try:
			self._dateDisplayFormatChoice.SetSelection(formats.dateFormats.index(config.conf["clockAndCalendar"]["dateDisplayFormat"]))
		except ValueError:
			pass
		self.input24HourFormatCheckBox.SetValue(config.conf["clockAndCalendar"]["input24HourFormat"])
		self._autoAnnounceChoice.SetSelection(config.conf["clockAndCalendar"]["autoAnnounce"])
		self._timeReportChoice.SetSelection(config.conf["clockAndCalendar"]["timeReporting"])
		self.quietHoursCheckBox.SetValue(config.conf["clockAndCalendar"]["quietHours"])
		self.quietStartTimeText.SetValue(config.conf["clockAndCalendar"]["quietHoursStartTime"])
		self.quietEndTimeText.SetValue(config.conf["clockAndCalendar"]["quietHoursEndTime"])
		self.checkAutoAnnounceSetup()
		self.checkQuietHoursSetup()

	def onSave(self):
		config.conf["clockAndCalendar"]["timeDisplayFormat"]=formats.timeFormats[self._timeDisplayFormatChoice.GetSelection()]
		config.conf["clockAndCalendar"]["dateDisplayFormat"]=formats.dateFormats[self._dateDisplayFormatChoice.GetSelection()]
		config.conf["clockAndCalendar"]["input24HourFormat"]=self.input24HourFormatCheckBox.GetValue()
		config.conf["clockAndCalendar"]["autoAnnounce"]=self._autoAnnounceChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeReporting"]=self._timeReportChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeReportSound"]=self._timeReportSoundChoice.GetStringSelection()
		config.conf["clockAndCalendar"]["quietHours"]=self.quietHoursCheckBox.GetValue()
		config.conf["clockAndCalendar"]["quietHoursStartTime"]=self.quietStartTimeText.GetValue()
		config.conf["clockAndCalendar"]["quietHoursEndTime"]=self.quietEndTimeText.GetValue()
