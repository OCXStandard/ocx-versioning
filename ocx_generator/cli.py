#  Copyright (c) 2023. OCX Consortium https://3docx.org. See the LICENSE
"""Script entry point."""
# System imports
from __future__ import annotations
import sys, warnings
# Third party
import typer
from typing_extensions import Annotated
from loguru import logger
from ocx_generator.utils.logging import LoguruHandler

# Project
from ocx_generator import __app_name__, __version__
from ocx_generator import generator

databinding = typer.Typer()

CONFIG_FILE = 'xsdata.xml'

logger.enable('ocx_generator')

# Logging config for application
config = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
        {"sink": str.join(__name__, ".log"), "serialize": True},
    ],
}

# Connect xsdata logger to loguru
# handler = LoguruHandler()
# logger.add(handler)


# Log warnings as well
# showwarning_ = warnings.showwarning

# handler.emit_warnings()


@databinding.command()
def generate(
    source: Annotated[
    str, typer.Argument(
    help=' The input source can be either a filepath, uri or a directory containing xml, json, xsd and wsdl files.')],
    package: Annotated[str, typer.Argument(help='The name of the databinding destination folder')],
    version: Annotated[str, typer.Argument(help='The source schema version number.')],
    config: Annotated[str, typer.Option(help='The generator config file', prompt=True)] = CONFIG_FILE,
    stdout: Annotated[bool, typer.Option(help='Print the output to the console.')] = False,
    recursive: Annotated[bool,
    typer.Option(help='Search files recursively in the source directory', prompt=True)] = False

):
    """Generate code from xml schemas, webservice definitions and any xml or json document.
       The input source can be either a filepath, uri or a directory containing  xml, json, xsd and wsdl files
    """
    result = generator.generate(source, package, version, config, stdout, recursive)



@databinding.command()
def version():
    """Print the version number and exit."""
    print(__version__)