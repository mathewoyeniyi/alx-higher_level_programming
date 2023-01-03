#!/usr/bin/python3
"""Define the height and width of a rectangle"""


class Rectangle:
    """Defines a rectangle.
        Private instance attribute: width.
        Instantiate with optional height.
    """
    def __init__(self, width=0, height=0):
        """Initialize the data conditions"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width to a value."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to a value."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Area of a rectangle
        :return: area of a rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Perimeter of a rectangle
        :return: perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """prints in stdout the area with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        hashes = []
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                hashes.append("#")
            if i != self.__height - 1:
                hashes.append("\n")
        return "".join(hashes)
