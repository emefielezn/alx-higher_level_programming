#!/usr/bin/python3

"""This module creates a class named Square"""


class Square:
    """A class named Square
    Attributes:
    attr1 (size): size of square
    """
    def __init__(self, size=0, position=(0,0)):
        """
        Args:
        size: size for __size attribute of class instance
        """
        self.__size = size
        self.__position = position
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

        if ((not isinstance(self.__position[0], int)) or not isinstance(self.__position[1], int))):
            raise TypeError("position must be a tuple of 2 positive integers")          elif (not isinstance(self.__position, tuple) or (self.__position[0] < 0) or (self.__position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")    
    @property
    def position(self):
    """ method to return a tuple of two positive integers                           """
    return (self.__position)
    @position.setter
    def position(self, value):
    """method to assign value to position                                           Args:                                                                           value: tuple value for position
    """                                                                             if ((not isinstance(self.__position[0], int)) or not isinstance(self.__position[1], int))):
        raise TypeError("position must be a tuple of 2 positive integers")
    elif (not isinstance(self.__position, tuple) or (self.__position[0] < 0) or (self.__position[1] < 0)):
        raise TypeError("position must be a tuple of 2 positive integers")
    else:
        self.__property = value

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
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            for x in range(self.__position[0]):
                print("-", end="")
            for y in range(self.__size):
                print("#", end="")
            print()
