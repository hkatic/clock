# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich and contributors
# Copyright 2013-2021, released under GPL.

import os
import glob
import addonHandler

PLUGIN_DIR = os.path.join (addonHandler.getCodeAddon ().path, "globalPlugins", "clock")
SOUNDS_DIR = os.path.join(PLUGIN_DIR, "waves")
LIST_SOUNDS = [os.path.split(path)[-1] for path in glob.glob(os.path.join(SOUNDS_DIR, '*.wav'))]
ALARMS_DIR = os.path.join(PLUGIN_DIR, "alarms")
LIST_ALARMS = [os.path.split(path)[-1] for path in glob.glob(os.path.join(ALARMS_DIR, '*.wav'))]
