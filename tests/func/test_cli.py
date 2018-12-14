#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import pytest

from typing import Any
from click import Command
from click.testing import CliRunner

from radick import Integer
from radixal import radify


@pytest.fixture(
    params=[
        pytest.param(
            i, id="BASE={:d}".format(i)
        ) for i in range(2, 37)
    ]
)
def base(request) -> int:
    return request.param


@pytest.fixture
def cli(base: int) -> Command:

    @click.command()
    @click.argument('parsed', type=Integer(base))
    def cli(parsed: int):
        click.echo(str(parsed), nl=False)

    return cli


def test_runner_with_valid_input(expected: int, base: int, cli: Command):

    runner = CliRunner()
    args = "-- " + radify(expected, base)
    result = runner.invoke(cli, args, catch_exceptions=True)

    assert result.exit_code == 0

    actual = int(result.output)

    assert actual == expected


def test_runner_with_invalid_input(unexpected: Any, cli: Command):

    runner = CliRunner()
    args = "-- {}".format(unexpected)
    result = runner.invoke(cli, args, catch_exceptions=True)

    with pytest.raises(SystemExit):

        assert result.exit_code > 0
        raise result.exception
