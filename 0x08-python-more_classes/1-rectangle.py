#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """Definition of the empty class Rectangle """
    def __init__(self, width=0; height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """private istance attribute : width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = ValueError

    @property
    def height(self):
        """private instance attribute : height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
