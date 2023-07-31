#!/usr/bin/env python3
"""
The module
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.requests.get')
    def test_org(self, org_name, mock_get):
        """
        Test the org() method of GithubOrgClient.

        :param org_name: The name of the GitHub organization to test.
        :param mock_get: Mock object of the requests.get method.
        """
        # Arrange
        org_url = f"https://api.github.com/orgs/{org_name}"
        expected_response = {"name": org_name, "url": org_url}
        instance = GithubOrgClient(org_name)
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        # Act
        result = instance.org()

        # Assert
        self.assertEqual(result, expected_response)


if __name__ == '__main__':
    unittest.main()
