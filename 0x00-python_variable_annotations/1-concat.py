#!/usr/bin/env python3
"""Here, we are required to write a type-annotated function concat 
   that takes a string str1 and a string str2 as arguments and returns a 
   concatenated string. This module would be imported by a
   function that concatenates two strings """


def concat(str1: str, str2: str) -> str:
    """
    Concatenates two strings and returns the result as a new string.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return str1 + str2
