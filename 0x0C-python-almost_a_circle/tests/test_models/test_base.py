#!/usr/bin/python3
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
import sys
from io import StringIO
import json
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

    def test_00_documentation(self):
        """
        Test to see if documentation is
        created and correct
        """
        pass
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
        bas = Base()
        self.assertEqual(bas.id, 5)

    def test_2_id(self):
        """
        Random arguments passed to check
        """
        t1 = Base(22)
        self.assertEqual(t1.id, 22)
        t2 = Base(-33)
        self.assertEqual(t2.id, -33)
        t3 = Base()
        self.assertEqual(t3.id, 6)

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

