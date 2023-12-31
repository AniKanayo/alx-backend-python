#!/usr/bin/env python3
"""
Module: 3-to_str
This module export a function to_str that takes a float n as
argument and returns the string representation of the float.
"""


def to_str(n: float) -> str:
    """
    Convert a float to its string representation.

    Args:
        n (float): The input float.

    Returns:
        str: The string representation of the input float.
    """
    return str(n)


if __name__ == "__main__":
    result = to_str(3.14)
    print(result == '3.14')
    print({'n': float, 'return': str})

# This file has now ended with a new line
