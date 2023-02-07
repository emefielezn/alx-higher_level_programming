#!/usr/bin/python3
"""This module defines a lookup function"""


def lookup(obj):
    """returns a valid list of attributes of the object"""
    return dir(obj)
