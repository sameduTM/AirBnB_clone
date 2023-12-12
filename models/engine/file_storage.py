#!/usr/bin/env python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
"""This is the file_storage module with class,
    FileStorage
"""


class FileStorage:
    """This is the FileStorage class that serializes instances to a,
    JSON file and deserializes JSON file to instances:
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as f:
            o_dict = {}
            for key, value in self.__objects.items():
                o_dict[key] = value.to_dict()
            json.dump(o_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                for ob in json.load(f).values():
                    self.new(eval(ob["__class__"])(**ob))
        else:
            return
