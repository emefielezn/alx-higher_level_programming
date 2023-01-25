#!/usr/bin/python3

"""This module creates a class named Square"""


class Square:
    """A class named Square
    Attributes:
    attr1 (size): size of square
    """
    def __init__(self, size=0):
        """
        Args:
        size: size for __size attribute of class instance
        """
        self.__size =size  
            if not (isinstance(self.__size, int)):
                raise TypeError("size must be an integer")
            if self. __size < 0:
                raise ValueError("size must be >= 0")
