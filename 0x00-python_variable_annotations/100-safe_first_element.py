#!/usr/bin/env python3
"""
Module: 100-safe_first_element
This prove exports a function that safes first element
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieve the first element of a list.

    Args:
        lst (Sequence[Any]): The input list of elements.

    Returns:
        Union[Any, None]: The 1st elemt of de list or None if the list is empty
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == "__main__":
    example_list = [1, 2, 3]
    result = safe_first_element(example_list)
    print(result)
