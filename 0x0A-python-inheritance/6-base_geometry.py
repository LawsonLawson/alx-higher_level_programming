#!/usr/bin/python3
"""
Module: 6-base_geometry

Description:
This module defines the class BaseGeometry, which includes a method 'area()'
that raises an exception indicating it is not implemented.

Class:
BaseGeometry - Class with a method 'area()' that raises an exception for not
being implemented.

"""


class BaseGeometry:
    """
    Class BaseGeometry: Incluleds a method 'area()' that raises an exception
    for not being implemented yet.
    """

    def area(self):
        """Not implemented yet."""
        raise Exception('area() is not implemented')
