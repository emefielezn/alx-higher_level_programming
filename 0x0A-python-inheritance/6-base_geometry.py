#!/usr/bin/python3
"""This module defines a class BaseGeometry"""


class BaseGeometry:
    """A class named BaseGeometry
    Attributes:
    attr1(area): Raises an exception
    """
    def area(self):
        """Raises an exception"""
        raise exception("area() is not implemented")
