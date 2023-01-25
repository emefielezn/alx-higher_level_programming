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

    @property
    def size(self):
        """Gets the size of the class instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the class instance"""
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
        self.__size = value

    def my_print(self):
        if (self.__size == 0):
            print()
            return
        else:
            for i in range(self.__size):
                print ('#', end="")
                for j in range(self.__size):
                    print("#", end="")
