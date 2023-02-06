#!/usr/bin/python3
"""This module defines a lookup function"""


def loopup(obj):
    """returns a valid list of attributes of the object"""
    return dir(obj)
