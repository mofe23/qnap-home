#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `qnap_home` package."""

import pytest

from click.testing import CliRunner

from qnap_home import qnap_home
from qnap_home import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get("https://github.com/audreyr/cookiecutter-pypackage")


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert "GitHub" in BeautifulSoup(response.content).title.string


def test_cli_root():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.cli)
    assert result.exit_code == 0
    assert "Console script for qnap_home" in result.output
    help_result = runner.invoke(cli.cli, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output


def test_cli_command():
    """Test a CLI command."""
    runner = CliRunner()
    result = runner.invoke(cli.command)
    assert result.exit_code == 0
    print(result.output)
    assert "A Command" in result.output
    help_result = runner.invoke(cli.command, ["--help"])
    assert help_result.exit_code == 0
    assert "--option INTEGER  An option" in help_result.output
