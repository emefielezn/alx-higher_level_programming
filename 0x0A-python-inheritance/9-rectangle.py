#!/usr/bin/python3
"""This module create a Rectangle class"""


BaeGeometry = __import__('7-base_geometry.py').BaseGeometry

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
    
    def area(self):
        """return area of Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """return string representation"""
        return "[Rectangle] {}/{}". format(self.__width, self.__height)
