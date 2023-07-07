#!/usr/bin/env python3
"""
This module provides a function to perform addition on two float numbers.
"""

import inspect
from typing import get_type_hints


def add(a: float, b: float) -> float:
    """
    Adds two float numbers and returns their sum.

    Args:
        a (float): The first float number.
        b (float): The second float number.

    Returns:
        float: The sum of the two float numbers.
    """
    return a + b
