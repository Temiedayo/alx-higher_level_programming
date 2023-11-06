#!/usr/bin/python3
"""defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """represent base geometry."""

    def area(self):
        """not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """authenticate a parameter as an integer.

        Args:
            name (str): The name
            value (int): The parameter
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
