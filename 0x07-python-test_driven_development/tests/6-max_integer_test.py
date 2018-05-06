#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_docstring(self):
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def test_func_doc(self):
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_emptyargs(self):
        self.assertIsNone(max_integer())

    def test_empty(self):
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer([None]), None)
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([2, 4, 5, 6, None])

    def test_one(self):
        self.assertEqual(max_integer([55]), 55)

    def test_integers(self):
        self.assertEqual(max_integer([1, 5, 6, 4]), 6)
        self.assertEqual(max_integer([55, 55, 55, 55]), 55)
        self.assertEqual(max_integer([6, 2, 3, 4]), 6)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([3]), 3)

    def test_integer_neg(self):
        self.assertEqual(max_integer([-44, -66, -43, -22]), -22)
        self.assertEqual(max_integer([1, 3, 74, -2]), 74)

    def test_float(self):
        self.assertEqual(max_integer([2.2, 3.3, 4.4, 5.5]), 5.5)
        self.assertEqual(max_integer([-44.5, -53.22, -2.224, -3.14]), -2.224)

    def test_string(self):
        self.assertEqual(max_integer("12345323121"), "5")
        self.assertEqual(max_integer("1, 2, 3"), "3")

    def test_alpha(self):
        self.assertEqual(max_integer(["xyz"]), "xyz")
        self.assertEqual(max_integer(["abc", "xyz"]), "xyz")
        self.assertEqual(max_integer(["abc", "1", "4", "xyz"]), "xyz")

    def test_other_type(self):
        self.assertEqual(max_integer([[1, 2, 3, 4], [1, 4, 3, 2]]), [1, 4, 3, 2])
        self.assertEqual(max_integer((3, 4, 5, 6, 19)), 19)
        with self.assertRaises(KeyError):
            max_integer({1: 1, 4: 5, 5: 4})

    def test_mix(self):
        with self.assertRaises(TypeError):
            max_integer(["help", 22, "44", 4.5, -3])
        with self.assertRaises(TypeError):
            max_integer(["help", [22], "44", 5.5, -55])

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main()
