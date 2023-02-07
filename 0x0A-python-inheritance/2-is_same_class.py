#!/usr/bin/python3
"""This module defines is_same_class function"""


def is_same_class(obj, a_class):
    """returns true or false based on inheritance"""

    return type(obj) == a_class
