#!/usr/bin/env python3


import unittest


class TestUtils(unittest.TestCase):

    def test_str(self):
        from code.demo import duplicate_value

        self.assertEqual("abab", duplicate_value("ab"))
        self.assertEqual(b"abab", duplicate_value(b"ab"))
        self.assertEqual(2, duplicate_value(1))
        self.assertLess(1, duplicate_value(1))
        self.assertIsNotNone(duplicate_value("anything"))
        # simulate a wrong case
        # self.assertEqual("abab", duplicate_value(b"ab"))

    def test_list(self):
        from code.demo import duplicate_value

        self.assertEqual([1, 1], duplicate_value([1]))
        self.assertIsNotNone(duplicate_value(["anything"]))
