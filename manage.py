import os
import sys
import click
import subprocess
from dotenv import load_dotenv


@click.group("App CLI")
def cli() -> None:
    pass


@cli.group(help="Run commands")
def run() -> None:
    pass


@cli.group(help="Check code styles ")
def check() -> None:
    pass


@check.command(help="Run the linter")
def styles() -> int:
    try:
        click.echo("Running `pylint`...")
        return subprocess.check_call(["pylint", "src"])
    except subprocess.CalledProcessError as ex:
        return 1
        # raise Exception(str(ex))


@check.command(help="Run the linter")
def types() -> int:
    try:
        click.echo("Running `mypy`...")
        return subprocess.check_call(["mypy", "."])
    except subprocess.CalledProcessError as ex:
        return 1
        # raise Exception(str(ex))


@run.command(help="Run the formatter")
def formatter() -> int:
    try:
        click.echo("Running `black`...")
        return subprocess.check_call(["black", "src"])
    except subprocess.CalledProcessError as ex:
        return 1
        # raise Exception(str(ex))


@run.command(help="Run pre-commit")
def precommit() -> int:
    try:
        click.echo("Running `pre-commit`...")
        subprocess.check_call(["pre-commit", "install"])
        return subprocess.check_call(["pre-commit", "run", "--all-files"])
    except subprocess.CalledProcessError as ex:
        return 1
        # raise Exception(str(ex))


if __name__ == "__main__":
    cli()
