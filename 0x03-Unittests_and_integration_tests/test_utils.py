#!/usr/bin/env python3
"""
This module contains TestAccessNestedMap class and the function to be tested
"""

import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple

def access_nested_map(nested_map: Dict[Any, Any], path: Tuple[Any]) -> Any:
    """Access nested map function"""
    for key in path:
        if key not in nested_map:
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Class for testing access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict[Any, Any], \
                               path: Tuple[Any], expected: Any) -> None:
        """
        Test method for access_nested_map function as required
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Dict[Any, Any], \
                                         path: Tuple[Any]) -> None:
        """Test method for access_nested_map function exception"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], path[-1])

if __name__ == '__main__':
    unittest.main()
