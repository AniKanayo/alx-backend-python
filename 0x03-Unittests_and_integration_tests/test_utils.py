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
    def test_access_nested_map(self, nested_map: Dict[Any, Any], \
                               path: Tuple[Any], expected: Any) -> None:
        """
        Test method for utils.access_nested_map function
        """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

if __name__ == '__main__':
    unittest.main()
