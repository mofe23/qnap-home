# -*- coding: utf-8 -*-

"""Console script for qnap_home."""
import sys
import click


@click.group()
def cli(args=None):
    """Console script for qnap_home."""
    click.echo("Replace this message by putting your code into "
               "qnap_home.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


@cli.command()
@click.option("-o", "--option", help="An option", default=10)
def command(option):
    click.echo(f"A Command with option {option}")


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
    print("DERE")
