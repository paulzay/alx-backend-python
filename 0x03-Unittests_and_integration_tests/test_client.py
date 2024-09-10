#!/usr/bin/env python3
"""test files for client.py"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock


class TestGithubOrgClient(unittest.TestCase):
    """ test case 1"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock):
        """ test org"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """ test public repos url"""
        with patch('client.GithubOrgClient.org') as mock:
            mock.return_value = {'repos_url': 'world'}
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class._public_repos_url, 'world')

    @patch('client.get_json')
    def test_public_repos(self, mock):
        """ test public repos"""
        json = [{"name": "google"}, {"name": "abc"}]
        mock.return_value = json
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=Mock) as mock_public:
            mock_public.return_value = 'hello'
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class.public_repos(), ['google', 'abc'])
            mock.assert_called_once_with('hello')
            mock_public.assert_called_once()

    @patch('client.get_json')
    def test_public_repos_with_license(self, mock):
        """ test public repos with license"""
        json = [{"name": "google", "license": {"key": "my_license"}},
                {"name": "abc"}]
        mock.return_value = json
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=Mock) as mock_public:
            mock_public.return_value = 'hello'
            test_class = GithubOrgClient('test')
            self.assertEqual(test_class.public_repos('my_license'), ['google'])
            mock.assert_called_once_with('hello')
            mock_public.assert_called_once()
