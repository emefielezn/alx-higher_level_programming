#!/usr/bin/python3
"""This module defines a class BaseGeometry"""


class BaseGeometry:
    """A class named BaseGeometry
    Attributes:
    attr1(area): Raises an exception
    """

    def area(self):
        """Raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
