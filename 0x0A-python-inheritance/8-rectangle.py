#!/usr/bin/python3
"""This module create a Rectangle class""


class Rectangle(BaseGeometry):
    """A class named Rectangle
    Attributes:
    attr1(width): width
    attr2(height): height
    """

    def __init__(self, wdith, height):
        """initialize rectangle instance"""

       self.integer_validator("width", width)
       self.integer_validator("height", height)
       self.__width = width
        self.__hieght = height
