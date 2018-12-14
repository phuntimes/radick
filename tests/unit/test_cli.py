#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import pytest

from typing import Any
from click import Command
from click.testing import CliRunner


@pytest.fixture
def cli() -> Command:

    @click.command()
    @click.argument('arg', type=click.INT)
    def cli(arg: int):
        click.echo(str(arg), nl=False)

    return cli


def test_runner_with_valid_input(expected: int, cli: Command):

    runner = CliRunner()
    args = "-- {:d}".format(expected)
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
