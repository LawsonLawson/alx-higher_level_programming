#!/usr/bin/python3
"""
Module: 7-base_geometry

Description:
This module defines the class BaseGeometry, which includes a method 'area()'
and 'integer_validator()'. A test suite for this module is available. Check.

Class:
BaseGeometry - Class with a method 'area()' and 'integer_validator()'.

"""


class BaseGeometry:
    """
    Class BaseGeometry: Incluleds a method 'area()' and 'integer_validator()'.

    Public Methods:
    - area
    - integer_validator
    """

    def area(self):
        """Not implemented yet."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validate the choice of value for name.

        Args:
        - name: A name (string).
        - value: Should be a positive integer.
        """
        if type(name) is not str:
            return
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
