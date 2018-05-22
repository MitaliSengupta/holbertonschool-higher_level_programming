#!/usr/bin/python3
"""
This module contains all unittest cases for
Base class
"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
import sys
from io import StringIO
import json
import os


class TestRectangle(unittest.TestCase):
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
        p = p8.check_files(['models/rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_00_documentation(self):
        """
        Test to see if documentation is
        created and correct
        """
        self.assertTrue(hasattr(Rectangle, "__init__"))
        self.assertTrue(Rectangle.__init__.__doc__)
        self.assertTrue(hasattr(Rectangle, "width"))
        self.assertTrue(Rectangle.width.__doc__)
        self.assertTrue(hasattr(Rectangle, "height"))
        self.assertTrue(Rectangle.height.__doc__)
        self.assertTrue(hasattr(Rectangle, "x"))
        self.assertTrue(Rectangle.x.__doc__)
        self.assertTrue(hasattr(Rectangle, "y"))
        self.assertTrue(Rectangle.y.__doc__)
        self.assertTrue(hasattr(Rectangle, "area"))
        self.assertTrue(Rectangle.area.__doc__)
        self.assertTrue(hasattr(Rectangle, "display"))
        self.assertTrue(Rectangle.display.__doc__)
        self.assertTrue(hasattr(Rectangle, "__str__"))
        self.assertTrue(Rectangle.__str__.__doc__)
        self.assertTrue(hasattr(Rectangle, "update"))
        self.assertTrue(Rectangle.update.__doc__)
        self.assertTrue(hasattr(Rectangle, "to_dictionary"))
        self.assertTrue(Rectangle.to_dictionary.__doc__)

    def test_0_id(self):
        """
        Tests for id
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(10, 11)
        R2 = Rectangle(11, 12, 13)
        R3 = Rectangle(12, 13, 14, 15)
        R6 = Rectangle(13, 14, 15, 16, 5)
        R4 = Rectangle(2, 4, 5, 6, 7)
        R5 = Rectangle(3, 45, 4, 2, id="10")
        self.assertEqual(R1.id, 1)
        self.assertEqual(R2.id, 2)
        self.assertEqual(R3.id, 3)
        self.assertEqual(R6.id, 5)
        self.assertEqual(R4.id, 7)
        self.assertEqual(R5.id, "10")

    def test_1_arg(self):
        """
        Test for checking numbers of
        objects
        """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Rectangle(10)
            Rectangle()
            Rectangle(x=10, y=20)

    def test_2_TypeError(self):
        """
        Test for check Type Error
        """
        Base._Base__nb_objects = 0
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 2)
            Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "Hello")
            Rectangle(True, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, "Hello")
            Rectangle(True, 2, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, "Hello")
            Rectangle(True, 2, 4, 5)

    def test_3_ValueError(self):
        """
        Test for checking value error
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-3, 2)
            Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(3, -2)
            Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 2, -2)
            Rectangle(1, 2, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 2, 2, -5)
            Rectangle(1, 2, 3, 0)

    def test_4_area(self):
        """
        This test is for testing the area
        method
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(1, 2)
        R2 = Rectangle(2, 3, 4)
        R3 = Rectangle(3, 4, 5, 6)
        R4 = Rectangle(4, 5, 6, 7, 8)
        R5 = Rectangle(9999999999999, 99999999999999)
        self.assertEqual(R1.area(), 2)
        self.assertEqual(R2.area(), 2 * 3)
        self.assertEqual(R3.area(), 3 * 4)
        self.assertEqual(R4.area(), 4 * 5)
        self.assertEqual(R5.area(), 9999999999999 * 99999999999999)

    def test_5_area(self):
        """
        Tests for less than 2 args
        """
        with self.assertRaises(TypeError):
            R = Rectangle()
            self.R.area(1)

    def test_6_display(self):
        """
        Test display method. Redirecting stdout to StringIO instance with
        expected output.
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(2, 4)
        R1O = "##\n" \
              "##\n" \
              "##\n" \
              "##\n"
        R2 = Rectangle(2, 3)
        R2O = "##\n" \
              "##\n" \
              "##\n"
        try:
            R1.display()
            self.assertEqual(sys.stdout.getvalue(), R1O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            R2.display()
            self.assertEqual(sys.stdout.getvalue(), R2O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_7_str(self):
        """
        Test that __str__ method produces correct output.
        """
        Base._Base__nb_objects = 0
        R0 = Rectangle(3, 2, 3)
        self.assertEqual(R0.__str__(), "[Rectangle] (1) 3/0 - 3/2")
        R1 = Rectangle(4, 5, 6, 7, 8)
        self.assertEqual(R1.__str__(), "[Rectangle] (8) 6/7 - 4/5")

    def test_8_display_with_xy(self):
        """
        Test display method. Redirecting stdout to StringIO instance with
        expected output.
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(2, 3, 2, 2)
        R1O = "\n" \
              "\n" \
              "  ##\n" \
              "  ##\n" \
              "  ##\n"
        R2 = Rectangle(3, 2, 1, 0)
        R2O = " ###\n" \
              " ###\n"
        try:
            R1.display()
            self.assertEqual(sys.stdout.getvalue(), R1O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)
        try:
            R2.display()
            self.assertEqual(sys.stdout.getvalue(), R2O)
        finally:
            sys.stdout.seek(0)
            sys.stdout.truncate(0)

    def test_9_update(self):
        """
        Test update method with *args
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(R1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        R1.update(*[8])
        self.assertEqual(R1.__str__(), "[Rectangle] (8) 10/10 - 10/10")
        R1.update(*[8, 7])
        self.assertEqual(R1.__str__(), "[Rectangle] (8) 10/10 - 7/10")
        R1.update(*[8, 7, 6])
        self.assertEqual(R1.__str__(), "[Rectangle] (8) 10/10 - 7/6")
        R1.update(*[8, 7, 6, 5])
        self.assertEqual(R1.__str__(), "[Rectangle] (8) 5/10 - 7/6")
        R1.update(*[8, 7, 6, 5, 4])
        self.assertEqual(R1.__str__(), "[Rectangle] (8) 5/4 - 7/6")
        with self.assertRaises(TypeError):
            R1.update(*[1, 1.0, 1, 1, 1])
        with self.assertRaises(TypeError):
            R1.update(*[1, "a"])
        with self.assertRaises(TypeError):
            R1.update(*[1, 1, 1.0])
        with self.assertRaises(TypeError):
            R1.update(*[1, 1, "a"])
        with self.assertRaises(TypeError):
            R1.update(*[1, 1, 1, [], 0])
        with self.assertRaises(TypeError):
            R1.update(*[1, 1, 1, 0, []])
        with self.assertRaises(ValueError):
            R1.update(*[1, 0])
        with self.assertRaises(ValueError):
            R1.update(*[1, 1, 0])
        with self.assertRaises(ValueError):
            R1.update(*[1, 1, 1, -1, 1])
        with self.assertRaises(ValueError):
            R1.update(*[1, 1, 1, 1, -1])

    def test_10_update2(self):
        """
        Test update() with **kwargs
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(1, 1, 1, 1)
        self.assertEqual(R1.__str__(), "[Rectangle] (1) 1/1 - 1/1")
        R1.update(**{'height': 10})
        self.assertEqual(R1.__str__(), "[Rectangle] (1) 1/1 - 1/10")
        R1.update(**{'width': 9, 'x': 8})
        self.assertEqual(R1.__str__(), "[Rectangle] (1) 8/1 - 9/10")
        R1.update(**{'y': 1, 'width': 2, 'x': 3, 'id': 89})
        self.assertEqual(R1.__str__(), "[Rectangle] (89) 3/1 - 2/10")
        R1.update(**{'x': 1, 'height': 2, 'y': 3, 'width': 4})
        self.assertEqual(R1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        R1.update(**{'wow': 3, 'hey': 'wow'})
        self.assertEqual(R1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        R1.update({'x': 10, 'height': 8})
        self.assertIs(type(R1.id), dict)

    def test_11_dict(self):
        """
        Test to_dictionary() method produces valid dictionary
        of Rectangle.
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(R1.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        self.assertEqual(R1.to_dictionary(), {'x': 1, 'y': 9,
                                              'id': 1, 'height': 2,
                                              'width': 10})
        self.assertIs(type(R1.to_dictionary()), dict)
        R2 = Rectangle(1, 1)
        self.assertEqual(R2.__str__(), "[Rectangle] (2) 0/0 - 1/1")
        R2.update(**R1.to_dictionary())
        self.assertEqual(R2.__str__(), "[Rectangle] (1) 1/9 - 10/2")
        self.assertNotEqual(R1, R2)

    def test_12_save_file_rect(self):
        """
        Test save_to_file() method of Rectangle to serialize
        and write to a file. Removes file after test if test
        was able to write to disk.
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(10, 7, 2, 8)
        R2 = Rectangle(2, 4)
        Rectangle.save_to_file([R1, R2])
        self.assertTrue(os.path.exists("Rectangle.json"), True)
        with open("Rectangle.json", mode='r') as myFile:
            self.assertEqual(json.loads(myFile.read()),
                             json.loads('[{"y": 8, '
                                        '"x": 2, '
                                        '"id": 1, '
                                        '"width": 10, '
                                        '"height": 7}, '
                                        '{"y": 0, '
                                        '"x": 0, '
                                        '"id": 2, '
                                        '"width": 2, '
                                        '"height": 4}]'))
        os.remove("Rectangle.json")

    def test_13_save_file_none(self):
        """
        Test save_to_file() method of Rectangle with None
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(10, 7, 2, 8)
        R2 = Rectangle(2, 4)
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"), True)
        with open("Rectangle.json", mode='r') as myFile:
            self.assertEqual(json.loads(myFile.read()),
                             json.loads('[]'))
        os.remove("Rectangle.json")

    def test_14_save_file_empty(self):
        """
        Test to_dictionary() method produces valid dictionary
        of Rectangle.
        """
        Base._Base__nb_objects = 0
        R1 = Rectangle(10, 7, 2, 8)
        R2 = Rectangle(2, 4)
        Rectangle.save_to_file([])
        self.assertIs(os.path.exists("Rectangle.json"), True)
        with open("Rectangle.json", mode='r') as myFile:
            self.assertEqual(json.loads(myFile.read()),
                             json.loads('[]'))
        os.remove("Rectangle.json")

    def test_15_load_file(self):
        """
        Test load from file if file non-existent
        """
        self.assertEqual(Rectangle.load_from_file(), [])
        Base._Base__nb_objects = 0
        R1 = Rectangle(1, 1)
        R2 = Rectangle(2, 2)
        Rectangle.save_to_file([R1, R2])
        Base._Base__nb_objects = 0
        RL = Rectangle.load_from_file()
        self.assertEqual(RL[0].to_dictionary(), R1.to_dictionary())
        self.assertEqual(RL[1].to_dictionary(), R2.to_dictionary())
