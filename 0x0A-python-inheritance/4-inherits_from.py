#!/usr/bin/python3
"""This module defines inherits_from function"""


def inherits_from(obj, a_class):
    """returns true or false based on inheritance"""

    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        False
