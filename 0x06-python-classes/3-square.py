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
        try:
            if not (isinstance(self.__size, int)):
                raise TypeError
        except TypeError:
            print("size must be an integer")
        try:
            if self.__size < 0:
                raise ValueError
        except ValueError:
            print("size must be >= 0")

    def area(self):
        """Calculates the area based on size of square
        Returns:
        int: The return value. Returns the area
        """
        return self.__size * self.__size
