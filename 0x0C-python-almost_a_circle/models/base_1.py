#!/usr/bin/python3
"""This class is the base class"""
import csv
import json
import turtle
import random


class Base:
    """Base class for all other modules
    Attributes:
        __nb_objects: private attribute to count objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of base class
        Args:
            id: input id
        Attributes:
            id: public instance id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json representation of the list_dictionary
        Args:
            list_dictionaries: input list of dictionary
        Returns:
            Json representation of the dictionary or empty when
            dictionary doesn't exist
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes Json representaiton to file
        Args:
            list_objs: input object to turn to json
        """
        new_list = []
        if list_objs is not None:
            new_list = [obs.to_dictionary() for obs in list_objs]
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """returns list represented by json
        Args:
            json_string: input json string
        Returns:
            list representation fo json
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attribute set
        Args:
            dictionary: dictionary inputed
        Returns:
            isntance with all the set attributes
        """
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        else:
            tmp = cls(1)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """laod the object from Json file
        Returns:
            This function will return the list of dictionart of the
            Json str representation
        """
        try:
            with open("{}.json".format(cls.__name__), 'r') as f:
                return [cls.create(**obj) for obj in
                        cls.from_json_string(f.read())]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes to CSV
        args:
            list_objs: list of objects input
        """
        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", 'x', 'y']
        else:
            fields = ["id", "size", 'x', 'y']
        with open("{}.csv".format(cls.__name__), 'w') as f:
            if list_objs is not None:
                dict_writer = csv.DictWriter(f, fields)
                dict_writer.writeheader()
                dict_writer.writerows([obj.to_dictionary()
                                       for obj in list_objs])
            else:
                dict_writer = csv.writer(f)
                dict_writer.writerow([[]])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes to CSV
        Returns:
            This function will return the list of dictionart of the
            CSV file
        """
        try:
            with open("{}.csv".format(cls.__name__), newline='') as f:
                dict_reader = csv.DictReader(f)
                new_list = []
                for line in dict_reader:
                    for key, item in line.items():
                        line[key] = int(item)
                    new_list.append(line)
                return [cls.create(**obj) for obj in new_list]
        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a widnow and draws all rectangels and squares
        args:
            list_rectangles: list of rectanlges input
            list_squares: list of squares input
        """
        turtle.getscreen()
        turtle.shape("turtle")
        for dic in list_rectangles + list_squares:
            turtle.pencolor(
                (random.random(), random.random(), random.random()))
            turtle.setpos(dic.x, dic.y)
            turtle.down()
            for i in range(2):
                turtle.forward(dic.height)
                turtle.left(90)
                turtle.forward(dic.width)
                turtle.left(90)
            turtle.up()
        turtle.exitonclick()
