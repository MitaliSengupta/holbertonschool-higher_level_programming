#!/usr/bin/python3
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
from io import StringIO
import json
import os
"""
This module contains all unittest cases for
Base class
"""


class TestBase(unittest.TestCase):
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
        p = p8.check_files(['models/base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_pep8_test(self):
        """
        Tests for pep8
        """
        p8 = pep8.StyleGuide(quiet=True)
        p = p8.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """test if docstring"""
        self.assertIsNotNone(Base.__doc__)

    def test_00_documentation(self):
        """
        Test to see if documentation is
        created and correct
        """
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertTrue(Base.load_from_file.__doc__)

    def test_0_id(self):
        """
        Test to check for id method
        """
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_1_id(self):
        """
        After run set of ids
        """
        Base._Base__nb_objects = 0
        bas = Base()
        self.assertEqual(bas.id, 1)

    def test_2_id(self):
        """
        Random arguments passed to check
        """
        Base._Base__nb_objects = 0
        t1 = Base(22)
        self.assertEqual(t1.id, 22)
        t2 = Base(-33)
        self.assertEqual(t2.id, -33)
        t3 = Base()
        self.assertEqual(t3.id, 1)

    def test_3_set_nb(self):
        """
        setting nb_objects as private
        """
        b = Base(33)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def test_4_dict(self):
        """
        Test to check if dictionary
        is working
        """
        r1 = Rectangle(10, 7, 2, 8, 1)
        d1 = r1.to_dictionary()
        j = {'x': 2, 'id': 1, 'y': 8, 'height': 7, 'width': 10}
        jd = Base.to_json_string([d1])
        self.assertEqual(d1, j)
        self.assertEqual(type(d1), dict)
        self.assertEqual(type(jd), str)

    def test_5_to_json_string(self):
        """
        Test to check for string to
        json conversion
        """
        Base.__nb_objects = 0
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertTrue(type(Base.to_json_string(None)) is str)
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertTrue(type(Base.to_json_string("[]")) is str)
        dt1 = {"id": 7, "width": 10, "height": 22, "x": 4, "y": 5}
        dt2 = {"id": 8, "width": 4, "height": 2, "x": 14, "y": 3}
        conv = Base.to_json_string([dt1, dt2])
        self.assertTrue(type(conv) is str)
        d = json.loads(conv)
        self.assertEqual(d, [dt1, dt2])

    def test_6_from_json_string(self):
        """
        Test to check from json to string
        conversion
        """
        s = '[{"id": 9, "width": 10, "height": 11, "x": 12, "y": 13}, \
{"id": 10, "width": 12, "height": 14, "x": 16, "y": 18}]'
        js = Base.from_json_string(s)
        self.assertTrue(type(js) is list)
        self.assertEqual(len(js), 2)

    def test_7_from_json_string_empty(self):
        """
        Test to check if it works with
        empty string or none
        """
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_8_jfile_empty(self):
        """Test to check from empty"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

    def test_9_jfile_None(self):
        """
        Test to check from none empty
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", mode="r") as myFile:
            self.assertEqual([], json.load(myFile))

    def test_10_rect(self):
        """
        Test to check for rectangle creation
        """
        R1 = Rectangle(4, 5, 6)
        R1_dict = R1.to_dictionary()
        R2 = Rectangle.create(**R1_dict)
        self.assertNotEqual(R1, R2)

    def test_11_sq(self):
        """
        Test to check for square creation
        """
        S1 = Square(44, 55, 66, 77)
        S1_dict = S1.to_dictionary()
        S2 = Rectangle.create(**S1_dict)
        self.assertNotEqual(S1, S2)

    def test_12_file_rect(self):
        """
        Test to check if file loads from rect
        """
        R1 = Rectangle(33, 34, 35, 26)
        R2 = Rectangle(202, 2)
        lR = [R1, R2]
        Rectangle.save_to_file(lR)
        lR2 = Rectangle.load_from_file()
        self.assertNotEqual(lR, lR2)

    def test_13_file_square(self):
        """
        Test to check if file loads from square
        """
        S1 = Square(22)
        S2 = Square(44, 44, 55, 66)
        lS = [S1, S2]
        Square.save_to_file(lS)
        lS2 = Square.load_from_file()
        self.assertNotEqual(lS, lS2)

    def test_14_csv_file(self):
        """
        Test to check for csv file
        """
        R1 = Rectangle(12, 13, 14, 15)
        R2 = Rectangle(3, 5)
        lR = [R1, R2]
        Rectangle.save_to_file_csv(lR)
        lR2 = Rectangle.load_from_file_csv()
        self.assertTrue(lR[0].__str__() == lR2[0].__str__())
        self.assertTrue(lR[1].__str__() == lR2[1].__str__())

    def test_15_csv_save_file(self):
        """
        Test to check for csv file with None and empty
        """
        Rectangle.save_to_file_csv(None)
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        os.remove("Rectangle.csv")
        self.assertEqual(Rectangle.load_from_file_csv(), [])
