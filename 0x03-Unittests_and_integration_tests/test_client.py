#!/usr/bin/env python3
"""
This module contains TestGithubOrgClient class for testing
the GithubOrgClient class in the client module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import client
from typing import Any


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing GithubOrgClient class."""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, test_org: str, mock_get_json: Mock) -> None:
        """Test method for GithubOrgClient.org method"""

        # Initialize GithubOrgClient with test_org
        github_org_client = client.GithubOrgClient(test_org)

        # Test that GithubOrgClient.org returns the correct value
        self.assertEqual(github_org_client.org, {"payload": True})

        # Test that get_json was called exactly once with the correct argument
        url = f"https://api.github.com/orgs/{test_org}"
        mock_get_json.assert_called_once_with(url)


if __name__ == '__main__':
    unittest.main()
