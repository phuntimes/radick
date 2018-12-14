#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from math import sqrt
from random import random
from typing import List, Iterator


def primes(n: int) -> List[int]:
    """
    Returns a list of primes < n.

    :param n: maximum value
    :returns: sequence of primes
    """
    sieve = [True] * n

    for i in range(3, int(sqrt(n)) + 1, 2):
        if sieve[i]:
            start = i * i
            step = 2 * i
            sieve[start::step] = [False] * ((n - i * i - 1) // (2 * i) + 1)

    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def values(n: int) -> Iterator[int]:
    """
    Generate test values (0 and primes).
    Sign of prime numbers is pseudo-random.

    :param n: maximum value
    :return: iterator of ints
    """
    yield 0
    for p in primes(n):
        yield -p if random() < 0.5 else p


@pytest.fixture(
    params=[
        pytest.param(
            i, id='EXPECTED={:d}'.format(i)
        ) for i in values(100)
    ]
)
def expected(request) -> int:
    return request.param


@pytest.fixture(
    params=[
        pytest.param(
            x, id="UNEXPECTED={!r}".format(x)
        ) for x in ("{foo}", b"{bar}", 3.14)
    ]
)
def unexpected(request):
    return request.param
