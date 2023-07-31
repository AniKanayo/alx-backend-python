#!/usr/bin/env python3
"""
This module contains TestAccessNestedMap and TestGetJson classes
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import utils


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


class TestGetJson(unittest.TestCase):
    """Class for testing utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload:
                      Dict[str, bool], mock_get: Mock) -> None:
        """
        Test method for utils.get_json function
        """
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = test_payload

        response = utils.get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)


if __name__ == '__main__':
    unittest.main()
