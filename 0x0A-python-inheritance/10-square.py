#!/usr/bin/python3
"""This module create a sqaure class"""


Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    """A class named square
    Attributes:
    attr1(size): size
    attr2(area): area
    """

    def __init__(self, wdith, height):
        """initialize rectangle instance"""
        
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
