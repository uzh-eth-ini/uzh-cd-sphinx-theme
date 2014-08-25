#!/usr/bin/env python
# -*- Mode: Python; py-indent-offset: 4; coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab

## Copyright (C) 2014, University of Zurich and ETH Zurich
## Copyright (C) 2014, Claudio Luck <cluck@ini.uzh.ch>

## Licensed under the terms of the MIT License, see LICENSE file.

from __future__ import print_function

import os

VERSION = (0, 1, 0)

__version__ = ".".join(str(v) for v in VERSION)
__version_full__ = __version__

def get_html_theme_path():
	"""Return list of HTML theme paths."""
	cur_dir = os.path.abspath(os.path.dirname(__file__))
	return [cur_dir]

