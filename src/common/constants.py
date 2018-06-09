# -*- coding: utf-8 -*-

"""
File containing all the constant variables
"""

import os
import json

__tmp = "data/config/path.cfg.json"
with open(__tmp, "r", encoding="utf-8") as f:
    CONFIG_PATH = json.load(f)
__tmp = "data/config/pictures.cfg.json"
with open(__tmp, "r", encoding="utf-8") as f:
    CONFIG_PICTURES = json.load(f)
__tmp = "data/config/ui.cfg.json"
with open(__tmp, "r", encoding="utf-8") as f:
    CONFIG_UI = json.load(f)

DIR_SRC = os.path.join(*CONFIG_PATH["folders"]["src"])  # Source files
DIR_DATA = os.path.join(*CONFIG_PATH["folders"]["data"])  # Data files
DIR_CONFIG = os.path.join(*CONFIG_PATH["folders"]["config"])  # Configuration files
DIR_PICTURES = os.path.join(*CONFIG_PATH["folders"]["pictures"])  # Pictures
