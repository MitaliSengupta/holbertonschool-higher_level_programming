#!/usr/bin/python3
"""
This module contains all unittest cases for
Base class
"""
import unittest
import pep8
from models.base import Base
from models.square import Square
import sys
from io import StringIO
import json
import os


class TestSquare(unittest.TestCase):
    """
    Class containing functions to run
    multiple tests
    """
    def setUp(self):
        """
        function to redirect stdout to check
        outpute of functions relying on print
        """
        sys.stdout = StringIO()

    def tearDown(self):
        """
        cleans everything up after running
        setup
        """
        sys.stdout = sys.__stdout__

    def test_pep8_model(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['models/square.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_00_documentation(self):
        """
        Test to see if documentation is
        created and correct
        """
        self.assertTrue(hasattr(Square, "__init__"))
        self.assertTrue(Square.__init__.__doc__)
        self.assertTrue(hasattr(Square, "size"))
        self.assertTrue(Square.size.__doc__)
        self.assertTrue(hasattr(Square, "x"))
        self.assertTrue(Square.x.__doc__)
        self.assertTrue(hasattr(Square, "y"))
        self.assertTrue(Square.y.__doc__)
        self.assertTrue(hasattr(Square, "__str__"))
        self.assertTrue(Square.__str__.__doc__)
        self.assertTrue(hasattr(Square, "update"))
        self.assertTrue(Square.update.__doc__)
        self.assertTrue(hasattr(Square, "to_dictionary"))
        self.assertTrue(Square.to_dictionary.__doc__)

    def test_0_id(self):
        """
        Testng for id
        """
        S1 = Square(1)
        S2 = Square(1, 2)
        S3 = Square(1, 2, 3)
        S4 = Square(1, 2, 3, 4)
        self.assertEqual(S2.x, 2)
        self.assertEqual(S3.y, 3)
        self.assertEqual(S4.id, 4)

    def test_1_nb(self):
        """
        Test for correct args
        """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(x=3, y=4)

    def test_2_TypeError(self):
        """
        Test for TypeErrors
        """
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("22")
            Square(-3)
            Square(True)
            Square(10.4)
            Square([3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {})
            Square(10, -3)
            Square(10, "blue")
            Square(10, 10.3)
            Square(10, False)
            Square(10, x=float(33))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 11, {})
            Square(10, 12, "blue")
            Square(10, 13, 10.3)
            Square(10, 22, -2)
            Square(10, 15, False)
            Square(10, 20, x=float(33))

    def test_2_ValueError(self):
        """
        Test for ValueErrors
        """
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-3)
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 14, -2)

    def test_3_str(self):
        """
        Test for __str__
        """
        Base._Base__nb_objects = 0
        S1 = Square(3)
        S2 = Square(3, 4)
        S3 = Square(3, 4, 5)
        self.assertEqual(S1.__str__(), "[Square] (1) 0/0 - 3")
        self.assertEqual(S2.__str__(), "[Square] (2) 4/0 - 3")
        self.assertEqual(S3.__str__(), "[Square] (3) 4/5 - 3")

    def test_4_area(self):
        """
        Test for area method
        """
        Base._Base__nb_objects = 0
        S1 = Square(3)
        S2 = Square(3, 4)
        S3 = Square(3, 4, 5)
        S4 = Square(232323232323232)
        self.assertEqual(S1.area(), 9)
        self.assertEqual(S2.area(), 9)
        self.assertEqual(S3.area(), 9)
        self.assertEqual(S4.area(), 232323232323232 ** 2)

    def test_5_display_xy(self):
        """
        Test display with offset
        """
        Base._Base__nb_objects = 0
        S1 = Square(4)
        S1O = "####\n" \
              "####\n" \
              "####\n" \
              "####\n"
        S2 = Square(3, 3)
        S2O = "   ###\n" \
              "   ###\n" \
              "   ###\n"
        S3 = Square(3, 2, 3)
        S3O = "\n\n\n" \
              "  ###\n" \
              "  ###\n" \
              "  ###\n"
        try:
            S1.display()
            self.assertEqual(sys.stdout.getvalue(), S1O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

        try:
            S2.display()
            self.assertEqual(sys.stdout.getvalue(), S2O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            S3.display()
            self.assertEqual(sys.stdout.getvalue(), S3O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_6_size(self):
        """
        Test to see if size works right
        """
        Base._Base__nb_objects = 0
        S1 = Square(3)
        self.assertEqual(S1.size, 3)
        self.assertEqual(S1.__str__(), "[Square] (1) 0/0 - 3")
        S1.size = 10
        self.assertEqual(S1.size, 10)
        self.assertEqual(S1.__str__(), "[Square] (1) 0/0 - 10")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            S1.size = "Gel"
            S1.size = 1.1
            S1.size = {1}
            S1.size = [1]
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            S1.size = 0
