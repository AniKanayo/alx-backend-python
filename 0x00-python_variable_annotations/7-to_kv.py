#!/usr/bin/env python3
"""Import modules """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with the square of the given int/float value.

    Args:
        k (str): The string key.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, float]: A tuple with the string key
        and the square of the int/float value.
    """
    return k, float(v ** 2)
