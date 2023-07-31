#!/usr/bin/env python3
"""
This module contains TestAccessNestedMap, TestGetJson, and
TestMemoize classes for testing the functions in the utils module.
"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
import utils
from typing import Any, Dict, Tuple


class TestGetJson(unittest.TestCase):
    """Class for testing utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict[str, Any],
                      mock_get: Mock) -> None:
        """Test method for utils.get_json function"""

        # Create a new Mock object with a json method that returns test_payload
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = test_payload

        # Call the function with the test_url
        response = utils.get_json(test_url)

        # Test that the mocked get method was called exactly
        # once with test_url as argument
        mock_get.assert_called_once_with(test_url)

        # Test that the output of get_json is equal to test_payload
        self.assertEqual(response, test_payload)


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
    def test_access_nested_map_exception(self, nested_map: Dict[Any, Any],
                                         path: Tuple[Any]) -> None:
        """Test method for utils.access_nested_map function exception"""
        with self.assertRaises(KeyError) as cm:
            utils.ac


class TestMemoize(unittest.TestCase):
    """Class for testing the memoize decorator."""

    def test_memoize(self):
        """Test method for the memoize decorator."""

        class TestClass:
            """Class for testing the memoize decorator."""

            def a_method(self) -> Any:
                """Returns 42"""
                return 42

            @utils.memoize
            def a_property(self) -> Any:
                """Returns the result of a_method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) \
                as mock_a_method:
            test_class_instance = TestClass()
            self.assertEqual(test_class_instance.a_property, 42)
            self.assertEqual(test_class_instance.a_property, 42)
            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
