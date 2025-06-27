#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with regular positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test with single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -1]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-10, -5, 0, 5, 10]), 10)

    def test_floats(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 1.2]), 2.7)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_middle(self):
        """Test when max is in the middle"""
        self.assertEqual(max_integer([1, 10, 2, 3]), 10)

    def test_max_at_end(self):
        """Test when max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_identical_elements(self):
        """Test with identical elements"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)


if __name__ == '__main__':
    unittest.main()