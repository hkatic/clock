# -*- coding: utf-8 -*-
# Clock Add-on for NVDA
# Author: Hrvoje Katich
# Copyright 2013-2018, released under GPL.

import os
import glob

PLUGIN_DIR = os.path.dirname(__file__)
SOUNDS_DIR = os.path.join(PLUGIN_DIR, "waves")
LIST_SOUNDS = [os.path.split(path)[-1] for path in glob.glob(os.path.join(SOUNDS_DIR, '*.wav'))]
ALARMS_DIR = os.path.join(PLUGIN_DIR, "alarms")
LIST_ALARMS = [os.path.split(path)[-1] for path in glob.glob(os.path.join(ALARMS_DIR, '*.wav'))]