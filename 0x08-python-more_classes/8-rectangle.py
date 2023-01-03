#!/usr/bin/python3
"""Define the height and width of a rectangle"""


class Rectangle:
    """Defines a rectangle.
        Private instance attribute: width.
        Instantiate with optional height.
        attribute:
        number of instance
        print_symbol
    """
    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize the data conditions"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                hashes.append(str(self.print_symbol))
            if i != self.__height - 1:
                hashes.append("\n")
        return "".join(hashes)

    def __repr__(self):
        """
        string representation of the rectangle
        to be able to recreate a new instance
        :return: the string representation
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        prints bye rectangle when an instance of a class is deleted
        :return: prints bye rectangle
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares and returns
        :param rect_1: first rectangle
        :param rect_2: second rectangle
        :return: the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
