#!/usr/bin/env python3
"""
Module: 9-element_length
This module exports a function that returns a list of tuples
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of sequences in a given iterable.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples containing the original
        sequences and their respective lengths.

    Example:
        >>> element_length(["hello", "world"])
        [('hello', 5), ('world', 5)]

    """
    return [(i, len(i)) for i in lst]
