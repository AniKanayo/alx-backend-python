#!/usr/bin/env python3
"""
Module: 102-type_checking.zoom_array
This module exports a function that zooms in on a given array and ...
"""
from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zoom in on the given array by repeating each element based on the
    specified factor.

    Args:
        lst (Tuple[int, ...]): The input array to zoom in on.
        factor (int, optional): The factor by which to repeat each element.
        Defaults to 2.

    Returns:
        List[int]: The zoomed-in array.

    Example:
        >>> zoom_array((12, 72, 91))
        [12, 12, 72, 72, 91, 91]

    """
    zoomed_in: List[int] = [
        item
        for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
