#!/usr/bin/python3
"""This module create a class MyInt"""


class MyInt(int):
    """A class named MyInt
    """

    def __eq__(self, other):
        """swap the equal buitin"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ swap the builtin ne"""
        return int.__eq__(self, other)
