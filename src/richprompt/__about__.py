#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Metadata for richprompt."""
# guard import as this is exec'd with runpy in setup.py so import will fail
try:
    from ._version import get_versions

    __version__ = get_versions()["version"]
    del get_versions
except ImportError:
    __version__ = None

__distname__ = "richprompt"
__name__ = "richprompt"
__description__ = "A better prompt for the IPython interactive shell" 
__license__ = "MIT license"
__copyright__ = "Copyright (c) 2019 Rich Lewis"

__author__ = "Rich Lewis"
__author_email__ = "opensource@richlew.is"

__url__ = "https://github.com/lewisacidic/richprompt"
__source_url__ = "https://github.com/lewisacidic/richprompt"
__bugtracker_url__ = "https://github.com/lewisacidic/richprompt/issues"
__download_url__ = "https://github.com/lewisacidic/richprompt/releases"

__classifiers__ = [
    "Development Status :: 2 - Pre-Alpha",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Natural Language :: English",
]

__keywords__ = ["ipython", "prompt"]

__all__ = [
    "__author__",
    "__author_email__",
    "__classifiers__",
    "__copyright__",
    "__description__",
    "__distname__",
    "__download_url__",
    "__keywords__",
    "__license__",
    "__name__",
    "__source_url__",
    "__url__",
    "__version__",
]
