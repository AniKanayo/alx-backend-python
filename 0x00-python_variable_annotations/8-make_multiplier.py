#!/usr/bin/env python3
"""
Module:8-make_multiplier
This module exports a function that that takes a float multiplier as argument
and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies
        a float by the multiplier.
    """
    def multiplier_func(num: float) -> float:
        """
        Multiply the given number by the multiplier.

        Args:
            num (float): The number to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return num * multiplier

    return multiplier_func
