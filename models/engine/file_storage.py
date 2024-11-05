#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    # path to json file
    __file_path = 'file.json'
    __objects = {}

    # ---------------------
    # added cls if object of specific class is given
    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        # show all objects
        if cls is None:
            return FileStorage.__objects
        # if cls show all objects of that class
        else:
            cls_objects = {key: value for key, value in FileStorage.__objects.items() if isinstance(value, cls)}
            return cls_objects
    # ----------------------

    # ------------------------
    def new(self, obj):
        """Adds new object to storage dictionary"""
        # creates a new object and puts it in storage
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj
    # -------------------------

    def save(self):
        """Saves storage dictionary to file"""
        # open a file in storage, save it,
        with open(FileStorage.__file_path, 'w') as f:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for key, val in tmp.items():
                tmp[key] = val.to_dict()
            json.dump(tmp, f)

    # ---------------------------
    def reload(self):
        """Loads storage dictionary from file"""
        try:
            # open file, load it, and put it in storage
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = key.split('.')[0]
                    cls = globals().get(cls_name)
                    if cls and value:
                        self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
        # ------------------------------------

    # -------------------------------
    def delete(self, obj=None):
        """ deletes an obj if there is one from __objects"""
        if obj is not None:
            # get name of class obj belongs to and its id
            key = f"{obj.__class__.__name__}.{obj.id}"
            # delete the obj from objects
            del FileStorage.__objects[key]
    # -------------------------------------

    # -------------------------------
    def close(self):
        """ call reloaad """
        self.reload()
    # -------------------------------------
