# -*- coding: utf-8 -*-

"""
File containing all the constant variables
"""

import os
import json

__config = "data/config/path.cfg.json"
with open(__config, "r", encoding="utf-8") as f:
    cfg = json.load(f)

DIR_SRC = os.path.join(*cfg["folders"]["src"])  # Source files
DIR_DATA = os.path.join(*cfg["folders"]["data"])  # Data files
DIR_CONFIG = os.path.join(*cfg["folders"]["config"])  # Configuration files
DIR_PICTURES = os.path.join(*cfg["folders"]["pictures"])  # Pictures
