#!/usr/bin/python3
"""0-lookup.py
"""


def lookup(obj):
    """ Function returning list of available attributes
        and methods of an object

    Args:
        obj: instance of the class

    Returns:
        List of attributes
    """

    return dir(obj)
