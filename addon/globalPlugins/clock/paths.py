# -*- coding: utf-8 -*-

"""
Clock Add-on for NVDA
@author: Hrvoje Katich <hrvojekatic@gmail.com>
@license: GNU General Public License version 2.0
"""

import os
import glob

PLUGIN_DIR = os.path.dirname(__file__)
SOUNDS_DIR = os.path.join(PLUGIN_DIR, "waves")
LIST_SOUNDS = [os.path.split(path)[-1] for path in glob.glob(os.path.join(SOUNDS_DIR, '*.wav'))]
