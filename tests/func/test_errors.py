#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from radick import Integer, InvalidTypeError, InvalidBaseError


@pytest.mark.parametrize(
    'base', [
        pytest.param(
            i, id="BASE={:d}".format(i)
        ) for i in (-1, 1, 37)
    ]
)
def test_init_with_invalid_base(base: int):

    with pytest.raises(InvalidBaseError):
        Integer(base)


@pytest.mark.parametrize(
    'base', [
        pytest.param(
            i, id="BASE={!r}".format(i)
        ) for i in (2.0, "foo", b"bar")
    ]
)
def test_init_with_invalid_type(base: int):

    with pytest.raises(InvalidTypeError):
        Integer(base)
