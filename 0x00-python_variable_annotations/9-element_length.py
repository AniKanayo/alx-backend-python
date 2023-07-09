#!/usr/bin/env python3
"""
Module: 9-element_length.element_length
This module exports a function that returns a list of tuples

"""
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """ A function that returns a list of tuples where the first element
    of each tuple is a string and the second is an integer
    """
    return [(i, len(i)) for i in lst]
