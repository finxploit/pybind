#! /usr/bin/env python

"""
    File name: console.py
    Author: Dimitar Petrov
    Date created: 2018/09/17
    Python Version: 3.6
    Description: Console Module
"""
from __future__ import unicode_literals, absolute_import, print_function
import click
from osiris-ext.utils import setup_logging



@click.command()
def main():
    """Example function with types documented in the docstring.

    Args:
    param1 (int): The first parameter.
    param2 (str): The second parameter.

    Returns:
    bool: The return value. True for success, False otherwise.
    """
    print('I am console')


if __name__ == "__main__":
    setup_logging()
    main()
