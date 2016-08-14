#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from mock import patch

from gitenberg.book import Book


class TestBookPath(unittest.TestCase):
    def setUp(self):
        with patch('github3.login') as login:
            self.login = login
            self.book = Book(3456)

    def test_remote_path(self):
        self.assertEqual(
            self.book.remote_path,
            "3/4/5/3456/"
        )

    def test_local_path(self):
        self.assertTrue(
            self.book.local_path.endswith("/3456")
        )

    def test_remote_path_below_ten(self):
        with patch('github3.login'):
            self.book = Book(7)
            self.assertEqual(
                self.book.remote_path,
                "7/"
            )
