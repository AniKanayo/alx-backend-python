#!/usr/bin/env python3
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
