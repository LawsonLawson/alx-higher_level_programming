#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_int = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer_positive_numbers(self):
        self.assertEqual(max_int([1, 2, 3, 4, 5]), 5)

    def test_max_integer_negative_numbers(self):
        self.assertEqual(max_int([-5, -3, -8, -2]), -2)

    def test_max_integer_mixed_numbers(self):
        self.assertEqual(max_int([-1, 0, 2, -3, 5]), 5)

    def test_max_integer_empty_list(self):
        self.assertIsNone(max_int([]))

    def test_max_integer_single_element_list(self):
        self.assertEqual(max_int([42]), 42)

    def test_max_integer_duplicate_values(self):
        self.assertEqual(max_int([3, 3, 3, 3]), 3)

    def test_max_integer_float_numbers(self):
        self.assertEqual(max_int([1.5, 2.7, 0.3, -2.5]), 2.7)

    def test_max_integer_mixed_types(self):
        with self.assertRaises(TypeError):
            max_int([1, 'two', 3, 4])

    def test_max_integer_nested_lists(self):
        self.assertEqual(max_int([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [7, 8, 9])

    def test_list_of_strings(self):
        string = ["Sinner", "won", "AO-2024", "RodLevarArena"]
        self.assertEqual(max_int(string), "won")

    def test_with_more_strings(self):
        self.assertEqual(max_int(["Jannik", "Sinner", "Medvedev"]), "Sinner")


if __name__ == '__main__':
    unittest.main()
