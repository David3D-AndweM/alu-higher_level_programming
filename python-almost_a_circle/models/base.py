#!/usr/bin/python3
"""base class"""
import json


class Base:
    """class named base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialising the init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json to string function"""
        if list_dictionaries is None:
            return "[]"

        if len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save file function"""
        fname = cls.__name__ + ".json"
        x = []
        if list_objs:
            for i in list_objs:
                x.append(cls.to_dictionary(i))

        with open(fname, mode="w") as saveme:
            saveme.write(cls.to_json_string(x))

    @staticmethod
    def from_json_string(json_string):
        """from json to string"""
        if json_string is None:
            return []

        if len(json_string) == 0:
            return []

        j_list = json.loads(json_string)
        return j_list

    @classmethod
    def create(cls, **dictionary):
        """create function"""
        if cls.__name__ == "Rectangle":
            dummy = cls(3, 2)
        if cls.__name__ == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file function"""
        try:
            with open(cls.__name__ + ".json", "r") as doc:
                document = doc.read()
        except FileNotFoundError:
            return []

        w = cls.from_json_string(document)
        x = []
        for z in w:
            x.append(cls.create(**z))
        return x
