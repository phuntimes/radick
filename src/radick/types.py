#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module defines replacement :class:`ParamType` for parsing strings containing
an integer value with arbitrary radix.
"""

__all__ = ["Integer"]
__version__ = '0.1.0'
__author__ = 'Sean McVeigh'

import attr

from typing import AnyStr
from click import ParamType, Parameter, Context
from .validators import is_int, is_base


@attr.s
class Integer(ParamType):
    """
    Replacement for integer :class:`ParamType` that allows specification of
    base conversion as specified in :class:`int`.
    """

    base: int = attr.ib(validator=[is_int, is_base])
    name: str = attr.ib(init=False, repr=False)

    def __attrs_post_init__(self):
        """
        Set dynamic :class:`ParamType` name.
        """
        self.name = "base {:d} integer".format(self.base)

    def convert(self, v: AnyStr, p: Parameter, c: Context) -> int:
        """
        Convert the string or bytes passed from command line arguments into
        a :class:`int` instance.

        :param v: parsed value passed
        :param p: parameter instance
        :param c: runtime context
        :return: converted value
        """
        try:
            return int(v, base=self.base)
        except (ValueError, UnicodeError):
            self.fail("{} is not a valid {}".format(v, self.name), p, c)
