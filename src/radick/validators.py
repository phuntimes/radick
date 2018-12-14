#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module defines common :class:`Attribute` validators.
"""

__all__ = ['is_int', 'is_base']
__version__ = '0.0.1'
__author__ = 'Sean McVeigh'

from attr import Attribute
from typing import Any, NoReturn
from .errors import InvalidTypeError, InvalidBaseError


def is_int(attrs: Any, attrib: Attribute, value: Any) -> NoReturn:
    """
    Check if passe value is integer.

    :param attrs: dataclass instance
    :param attrib: field instance
    :param value: passed value
    :raises ValueError: if not valid
    """
    if not isinstance(value, int):
        raise InvalidTypeError(attrib, int, value)


def is_base(attrs: Any, attrib: Attribute, value: int) -> NoReturn:
    """
    Check if passed value is a valid integer base.

    :param attrs: dataclass instance
    :param attrib: field instance
    :param value: passed value
    :raises ValueError: if not valid
    """
    if value < 0 or value == 1 or value > 36:
        raise InvalidBaseError(attrib, value)
