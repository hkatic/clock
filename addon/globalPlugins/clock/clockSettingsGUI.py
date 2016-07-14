# -*- coding: utf-8 -*-

"""
Clock Add-on for NVDA
@author: Hrvoje Katich <hrvojekatic@gmail.com>
@license: GNU General Public License version 2.0
"""

from datetime import datetime
import paths
import formats
import config
import nvwave
import gui
import os
import wx

class clockSettingsDialog(gui.SettingsDialog):
	title=_("Clock Settings")

	def __init__(self, parent):
		super(clockSettingsDialog, self).__init__(parent)

	def makeSettings(self, sizer):

		#combo box for time display format
		timeDisplaySizer=wx.BoxSizer(wx.HORIZONTAL)
		timeDisplayFormatLabel=wx.StaticText(self, label=_("&Time display format:"))
		timeDisplaySizer.Add(timeDisplayFormatLabel)
		self._timeDisplayFormatChoice=wx.Choice(self, choices=[datetime.now().strftime(x) for x in formats.timeDisplayFormats])
		timeDisplaySizer.Add(self._timeDisplayFormatChoice)
		sizer.Add(timeDisplaySizer)

		#combo box for date display format
		dateDisplaySizer=wx.BoxSizer(wx.HORIZONTAL)
		dateDisplayFormatLabel=wx.StaticText(self, label=_("&Date display format:"))
		dateDisplaySizer.Add(dateDisplayFormatLabel)
		self._dateDisplayFormatChoice=wx.Choice(self, choices=[datetime.now().strftime(x) for x in formats.dateDisplayFormats])
		dateDisplaySizer.Add(self._dateDisplayFormatChoice)
		sizer.Add(dateDisplaySizer)

		#check box for 24-hour input
		self.input24HourFormatCheckBox=wx.CheckBox(self, label=_("Input in &24-hour format"))

		#combo box for automatic time announcement
		autoAnnounceSizer=wx.BoxSizer(wx.HORIZONTAL)
		autoAnnounceLabel=wx.StaticText(self, label=_("Auto announce &interval:"))
		autoAnnounceSizer.Add(autoAnnounceLabel)
		autoAnnounceChoices=(_("off"), _("every 10 minutes"), _("every 15 minutes"), _("every 30 minutes"), _("every hour"))
		self._autoAnnounceChoice=wx.Choice(self, choices=autoAnnounceChoices)
		self._autoAnnounceChoice.Bind(wx.EVT_CHOICE, self.onAutoAnnounce)
		autoAnnounceSizer.Add(self._autoAnnounceChoice)
		sizer.Add(autoAnnounceSizer)

		#combo box for time reporting
		timeReportSizer=wx.BoxSizer(wx.HORIZONTAL)
		timeReportLabel=wx.StaticText(self, label=_("Time &announcement:"))
		timeReportSizer.Add(timeReportLabel)
		timeReportChoices=(_("speech and sound"), _("speech only"), _("sound only"))
		self._timeReportChoice=wx.Choice(self, choices=timeReportChoices)
		timeReportSizer.Add(self._timeReportChoice)
		sizer.Add(timeReportSizer)

		#combo box for chime sound
		timeReportSoundSizer=wx.BoxSizer(wx.HORIZONTAL)
		timeReportSoundLabel=wx.StaticText(self, label=_("Clock chime &sound:"))
		timeReportSoundSizer.Add(timeReportSoundLabel)
		self._timeReportSoundChoice=wx.Choice(self, choices=paths.LIST_SOUNDS)
		self._timeReportSoundChoice.SetStringSelection(config.conf["clockAndCalendar"]["timeReportSound"])
		self._timeReportSoundChoice.Bind(wx.EVT_CHOICE, self.onSoundSelected)
		timeReportSoundSizer.Add(self._timeReportSoundChoice)
		sizer.Add(timeReportSoundSizer)

		#quiet hours sizer
		self.quietHoursSizer=wx.BoxSizer(wx.VERTICAL)

		#check box for quiet hours
		self.quietHoursCheckBox=wx.CheckBox(self, label=_("&Quiet hours"))
		self.quietHoursCheckBox.Bind(wx.EVT_CHECKBOX, self.onQuietHoursToggle)
		self.quietHoursSizer.Add(self.quietHoursCheckBox)

		#edit box for quiet hours start time
		self.quietStartTimeSizer=wx.BoxSizer(wx.HORIZONTAL)
		quietStartTimeLabel=wx.StaticText(self, label=_("Quiet hours start time:"))
		self.quietStartTimeSizer.Add(quietStartTimeLabel)
		self.quietStartTimeText=wx.TextCtrl(self)
		self.quietStartTimeSizer.Add(self.quietStartTimeText)
		self.quietHoursSizer.Add(self.quietStartTimeSizer)

		#edit box for quiet hours end time
		self.quietEndTimeSizer=wx.BoxSizer(wx.HORIZONTAL)
		quietEndTimeLabel=wx.StaticText(self, label=_("Quiet hours end time:"))
		self.quietEndTimeSizer.Add(quietEndTimeLabel)
		self.quietEndTimeText=wx.TextCtrl(self)
		self.quietEndTimeSizer.Add(self.quietEndTimeText)
		self.quietHoursSizer.Add(self.quietEndTimeSizer)
		sizer.Add(self.quietHoursSizer)

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
			self.quietHoursSizer.ShowItems(show=False)
		else:
			self.quietHoursSizer.ShowItems(show=True)

	def checkQuietHoursSetup(self):
		if self.quietHoursCheckBox.GetValue() and self.quietHoursSizer.IsShown(True):
			self.quietStartTimeSizer.ShowItems(show=True)
			self.quietEndTimeSizer.ShowItems(show=True)
		elif not self.quietHoursCheckBox.GetValue() and self.quietHoursSizer.IsShown(True):
			self.quietStartTimeSizer.ShowItems(show=False)
			self.quietEndTimeSizer.ShowItems(show=False)

	def postInit(self):
		self._timeDisplayFormatChoice.SetSelection(formats.timeDisplayFormats.index(config.conf["clockAndCalendar"]["timeDisplayFormat"]))
		self._timeDisplayFormatChoice.SetFocus()
		self._dateDisplayFormatChoice.SetSelection(formats.dateDisplayFormats.index(config.conf["clockAndCalendar"]["dateDisplayFormat"]))
		self.input24HourFormatCheckBox.SetValue(config.conf["clockAndCalendar"]["input24HourFormat"])
		self._autoAnnounceChoice.SetSelection(config.conf["clockAndCalendar"]["autoAnnounce"])
		self._timeReportChoice.SetSelection(config.conf["clockAndCalendar"]["timeReporting"])
		self.quietHoursCheckBox.SetValue(config.conf["clockAndCalendar"]["quietHours"])
		self.quietStartTimeText.SetValue(config.conf["clockAndCalendar"]["quietHoursStartTime"])
		self.quietEndTimeText.SetValue(config.conf["clockAndCalendar"]["quietHoursEndTime"])
		self.checkAutoAnnounceSetup()
		self.checkQuietHoursSetup()

	def onOk(self, evt):
		super(clockSettingsDialog, self).onOk(evt)
		config.conf["clockAndCalendar"]["timeDisplayFormat"]=formats.timeDisplayFormats[self._timeDisplayFormatChoice.GetSelection()]
		config.conf["clockAndCalendar"]["dateDisplayFormat"]=formats.dateDisplayFormats[self._dateDisplayFormatChoice.GetSelection()]
		config.conf["clockAndCalendar"]["input24HourFormat"]=self.input24HourFormatCheckBox.GetValue()
		config.conf["clockAndCalendar"]["autoAnnounce"]=self._autoAnnounceChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeReporting"]=self._timeReportChoice.GetSelection()
		config.conf["clockAndCalendar"]["timeReportSound"]=self._timeReportSoundChoice.GetStringSelection()
		config.conf["clockAndCalendar"]["quietHours"]=self.quietHoursCheckBox.GetValue()
		config.conf["clockAndCalendar"]["quietHoursStartTime"]=self.quietStartTimeText.GetValue()
		config.conf["clockAndCalendar"]["quietHoursEndTime"]=self.quietEndTimeText.GetValue()
