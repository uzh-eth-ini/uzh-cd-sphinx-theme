#!/usr/bin/env python
# -*- Mode: Python; py-indent-offset: 4; coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 expandtab

## Copyright (C) 2014, University of Zurich and ETH Zurich
## Copyright (C) 2014, Claudio Luck <cluck@ini.uzh.ch>

## Licensed under the terms of the MIT License, see LICENSE file.

import os

from setuptools import setup, find_packages

from sphinx_uzh_cd_theme import __version__


# Don't copy Mac OS X resource forks on tar/gzip.
os.environ['COPYFILE_DISABLE'] = "true"

# Packages.
MOD_NAME = "sphinx_uzh_cd_theme"
PKGS = [x for x in find_packages() if x.split('.')[0] == MOD_NAME]


def read_file(name):
    """Read file name (without extension) to string."""
    cur_path = os.path.dirname(__file__)
    exts = ('txt', 'rst')
    for ext in exts:
        path = os.path.join(cur_path, '.'.join((name, ext)))
        if os.path.exists(path):
            with open(path, 'rt') as file_obj:
                return file_obj.read()

    return ''


setup(
    name="sphinx-uzh-cd-theme",
    version=__version__,
    use_2to3=True,
    description="Sphinx Theme following the UZH Corporate Design",
    long_description=read_file("README.md"),
    url="http://it.ini.uzh.ch",

    author="Claudio Luck",
    author_email="claudio.luck@ini.uzh.ch",

    classifiers=[
        #"Development Status :: 5 - Production/Stable",
	'Development Status :: 3 - Alpha',
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        #"Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation",
    ],

    install_requires=[
        "setuptools",
    ],

    packages=PKGS,
    include_package_data=True,
)

