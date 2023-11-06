#!/usr/bin/python3
"""defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """initialize new Rectangle.

        Args:
            width (int): The width
            height (int): The height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
