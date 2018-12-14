#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module defines specific errors with predefined error messages.
"""

__all__ = ["InvalidTypeError", "InvalidBaseError"]
__version__ = '0.1.2'
__author__ = 'Sean McVeigh'


from attr import Attribute
from typing import Type, Any


class InvalidTypeError(TypeError):
    """
    A :class:`ValueError` to denote an invalid type of the value passed
    to an :class:`Attribute`.
    """

    def __init__(self, attrib: Attribute, valid: Type, value: Any):
        """
        Format the message with dataclass context.

        :param attrib: field instance
        :param valid: expected type
        :param value: passed value
        """

        msg = "'{name}' must be an {valid!r}, not a {invalid!r}".format(
            name=attrib.name,
            valid=valid,
            invalid=type(value)
        )

        super(InvalidTypeError, self).__init__(msg, attrib, value)


class InvalidBaseError(ValueError):
    """
    A :class:`ValueError` to denote an invalid integer base passed as a
    value to an :class:`Attribute`.
    """

    def __init__(self, attrib: Attribute, value: Any):
        """
        Format the message with dataclass context.

        :param attrib: field instance
        :param value: passed value
        """

        msg = "'{name}' must be 0 or 2-36, not {value!r}".format(
            name=attrib.name,
            value=value
        )

        super(InvalidBaseError, self).__init__(msg, attrib, value)
