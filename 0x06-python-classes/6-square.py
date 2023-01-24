#!/usr/bin/python3

"""This module creates a class named Square"""


class Square:
    """A class named Square
    Attributes:
    attr1 (size): size of square
    """

    def __init__(self, size):

    """
    Args:
    size: size for __size attribute of class instance
    """

    self type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size

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

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the # character"""

        if self.__size > 0:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                    print()
                else:
                    print()

    @property
    def position(self):
        """Gets the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""

        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
