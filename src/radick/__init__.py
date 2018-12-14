#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Extension library for :ref:`click` that replaces the integer parameter type
with :class:`Integer`, which supports parsing string values of arbitrary radix.

This allows parsing of, for example, hexadecimal strings like `0xFF` or binary
strings `0b100` from command line arguments to be interpret as :class:`int`.

Additionally, :data:`BIN`, :data:`INT`, :data:`OCT`, :data:`HEX`, and
:data:`PRE` are provided for convenience for bases 2, 8, 10 , 16, and 0
(interpret from prefix, i.e. `0b`, `0o`, or `0x`) respectively.
"""

__all__ = [
    'Integer', 'InvalidBaseError', 'InvalidTypeError',
    'PRE', 'BIN', 'OCT', 'INT', 'HEX'
]
__version__ = '0.1.3'
__author__ = 'Sean McVeigh'

from .types import Integer
from .errors import InvalidBaseError, InvalidTypeError


PRE = Integer(0)
BIN = Integer(2)
OCT = Integer(8)
INT = Integer(10)
HEX = Integer(16)
