# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

import os
import glob
import addonHandler
import globalVars
from typing import Callable

addonHandler.initTranslation()
_: Callable[[str], str]

PLUGIN_DIR = os.path.join(addonHandler.getCodeAddon().path, "globalPlugins", "clock")
SOUNDS_DIR = os.path.join(PLUGIN_DIR, "waves")
ALARMS_DIR = os.path.join(PLUGIN_DIR, "alarms")
CUSTOM_SOUNDS_DIR = os.path.join(globalVars.appArgs.configPath, "clock_sounds")
CUSTOM_ALARMS_DIR = os.path.join(CUSTOM_SOUNDS_DIR, "alarm")
CUSTOM_CLOCK_TIME_DIR = os.path.join(CUSTOM_SOUNDS_DIR, "clock_time")

for path in [CUSTOM_SOUNDS_DIR, CUSTOM_ALARMS_DIR, CUSTOM_CLOCK_TIME_DIR]:
	if not os.path.exists(path):
		os.makedirs(path)

LIST_SOUNDS = [os.path.split(path)[-1] for path in glob.glob(os.path.join(SOUNDS_DIR, '*.wav'))]
LIST_SOUNDS.extend([os.path.split(path)[-1] for path in glob.glob(os.path.join(CUSTOM_CLOCK_TIME_DIR, '*.wav'))])

LIST_ALARMS = [os.path.split(path)[-1] for path in glob.glob(os.path.join(ALARMS_DIR, '*.wav'))]
LIST_ALARMS.extend([os.path.split(path)[-1] for path in glob.glob(os.path.join(CUSTOM_ALARMS_DIR, '*.wav'))])

# Translators: This is a choice in a list of sounds.
CUSTOM_SOUND = _("Custom")

