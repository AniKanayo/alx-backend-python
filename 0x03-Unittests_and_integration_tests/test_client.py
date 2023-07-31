#!/usr/bin/env python3
"""
This module contains TestGithubOrgClient class for testing
the GithubOrgClient class in the client module.
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import client
from typing import Any


class TestGithubOrgClient(unittest.TestCase):
    """Class for testing GithubOrgClient class."""

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org: PropertyMock) -> None:
        """
        Test method for GithubOrgClient._public_repos_url property.
        This method tests that GithubOrgClient._public_repos_url
        returns the correct value.
        """
        # Setup the mock property
        mock_org.return_value = {
            "login": "google",
            "id": 1342004,
            "public_repos": 5,
            "repos_url": "https://api.github.com/users/google/repos"
        }

        # Initialize GithubOrgClient with test_org
        github_org_client = client.GithubOrgClient("google")

        # Test that GithubOrgClient._public_repos_url returns the correct value
        expected_url = "https://api.github.com/users/google/repos"
        self.assertEqual(github_org_client._public_repos_url, expected_url)

if __name__ == '__main__':
