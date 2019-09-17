#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis <opensource@richlew.is>
"""
richprompt.load
~~~~~~~~~~~~~~~

A means of loading richprompt without magic.
"""

from IPython import get_ipython
from . import magic


ip = get_ipython()


def load():
    magic.load_ipython_extension(ip)


def unload():
    magic.unload_ipython_extension(ip)
