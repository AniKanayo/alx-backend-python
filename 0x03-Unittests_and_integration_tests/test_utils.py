#!/usr/bin/env python3
"""Module for testing the function access_nested_map"""
import unittest
from parameterized import parameterized


def access_nested_map(nested_map: dict, path: tuple) -> object:
    """Accesses a value in a nested map.

    Args:
        nested_map (dict): The nested map.
        path (tuple): The path to the value in the map.

    Returns:
        object: The value that is at the given path in the map.
    """
    # Assuming this function is already implemented
    pass


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing the function access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests the function access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
