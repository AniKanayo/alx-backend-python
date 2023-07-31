#!/usr/bin/env python3
"""
This module contains the TestMemoize class for
testing the memoize decorator.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import memoize
from typing import Any


class TestMemoize(unittest.TestCase):
    """Class for testing the memoize decorator."""

    def test_memoize(self):
        """Test method for the memoize decorator."""

        class TestClass:
            """Class for testing the memoize decorator."""

            def a_method(self) -> Any:
                """Returns 42"""
                return 42

            @memoize
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
