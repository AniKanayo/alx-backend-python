#!/usr/bin/env python3

"""
Module: 101-safely_get_value.safely_get_value
This module exports a function that safely gets a value from a dictionary
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary based on the given key.

    Args:
        dct (Mapping): A dictionary-like object.
        key (Any): The key to look for in the dictionary.
        default (Union[T, None], optional): The default value to
        return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value associated with the key in the dictionary,
        or the default value if the key is not found.

    Example:
        >>> safely_get_value({'a': 1, 'b': 2}, 'b', default=0)
        2

    """
    if key in dct:
        return dct[key]
    else:
        return default
