#!/usr/bin/python3
"""
This module contains the function say_my_name that prints a formatted full name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Args:
        first_name (str): first name
        last_name (str): last name (default is empty string)

    Raises:
        TypeError: if first_name or last_name is not a string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
