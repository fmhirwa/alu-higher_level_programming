#!/usr/bin/python3
""""Documented"""


import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInt(unittest.TestCase):
    """" Test Cases"""

    def test_simple_case(self):
        """"Documented"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_case(self):
        """"Documented"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty_case(self):
        """"Documented"""
        self.assertEqual(max_integer([]), None)

    def test_max_middle_case(self):
        """"Documented"""
        self.assertEqual(max_integer([7, 2, 8, 3, 4]), 8)

    def test_one_element_case(self):
        """"Documented"""
        self.assertEqual(max_integer([5]), 5)
