#!/usr/bin/python3
"""This module defines a class named MyList"""


class MyList(list):
    """A class named MyList
    Attributes:
    attr1(print_sorted): prints sorted list
    """
    def print_sorted(self):
        """prints instance"""
        print(sorted(self))
