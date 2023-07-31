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

    @patch('client.get_json', return_value=[{"name": "repo1"},
           {"name": "repo2"}])
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """
        Test method for GithubOrgClient.public_repos method.
        This method tests that GithubOrgClient.public_repos returns
        the correct value.
        """
        with patch('client.GithubOrgClient._public_repos_url',
                    new_callable=PropertyMock) as mock_public_repos_url:
            # Setup the mock property
            mock_public_repos_url.return_value = "https://api.github.com/"
           "users/google/repos"

            # Initialize GithubOrgClient with test_org
            github_org_client = client.GithubOrgClient("google")

            # Test that GithubOrgClient.public_repos returns the correct value
            expected_repos = ["repo1", "repo2"]
            self.assertEqual(github_org_client.public_repos, expected_repos)

            # Test that the mocked property and the mocked get_json was
            # called once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()


if __name__ == '__main__':
    unittest.main()
