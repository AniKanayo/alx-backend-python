#!/usr/bin/env python3
"""
This module contains TestAccessNestedMap class
"""

import unittest
from parameterized import parameterized
import utils
from typing import Any, Dict, Tuple

class TestAccessNestedMap(unittest.TestCase):
    """Class for testing utils.access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict[Any, Any],
                               path: Tuple[Any], expected: Any) -> None:
        """
        Test method for utils.access_nested_map function
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map:
                                         Dict[Any, Any], path: Tuple[Any]) -> None:
        """Test method for utils.access_nested_map function exception"""
        with self.assertRaises(KeyError) as cm:
            utils.access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"{' -> '.join(path)} not found in nested_map")

if __name__ == '__main__':
    unittest.main()
