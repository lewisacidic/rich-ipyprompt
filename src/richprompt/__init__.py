#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""A better prompt for the IPython interactive shell.

See `richprompt.__about__` for more info.
"""

from .__about__ import __copyright__
from .__about__ import __distname__
from .__about__ import __license__
from .__about__ import __url__
from .__about__ import __version__
from .magic import load_ipython_extension
from .magic import unload_ipython_extension
from .prompts import RichPrompts
from .startup import load
from .startup import unload
from .timer import Timer

__all__ = [
    "__copyright__",
    "__distname__",
    "__license__",
    "__url__",
    "__version__",
    "load",
    "load_ipython_extension",
    "RichPrompts",
    "Timer",
    "unload",
    "unload_ipython_extension",
]
