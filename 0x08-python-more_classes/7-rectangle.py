#!/usr/bin/python3
"""This module creates a class named Rectangle"""

class Rectangle:
    """A class named Rectangle
    Attributes:
    attr1(width): width of rectangle
    attr2(height): height of rectangle
    attr3(number_of_instances):no of instances
    attr4(print_symbol): symbol for representation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the class instance"""
        return self.__width
    @width.setter
    def width(self, value):
        """Sets the width of the class instance"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the class instance"""
        return self.__height
    @height.setter
    def height(self, value):
        """Sets the height of the class instance"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the class instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the permimeter of the class instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        """ print() __str__ method funtion to return rectangle in char '#'
        """
        res = ""
        if self.__width == 0 or self.__height == 0:
            return res
        for i in range(self.__height):
            res += str(self.print_symbol)
            if i == self.__height - 1:
                res += ('#' * self.__width)
            else:
                res += (('#' * self.__width) + '\n')
                return res

    def __repr__(self):
        """ print() or eval() __repr__ method function to return
        Rectangle(width, height)
        """
        w = str(self.__width)
        h = str(self.__height)
        res = "Rectangle(" + w + ", " + h + ")"
        return res

    def __del__(self):
        """ Print a message for del"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
