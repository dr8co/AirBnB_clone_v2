#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format
    Attributes:
        __file_path (str): path to the JSON file (ex: file.json)
        __objects (dict): empty but will store all objects by <class name>.id"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if not cls:
            return FileStorage.__objects
        results = {}
        for k, v in FileStorage.__objects.items():
            if k.split('.')[0] == cls.__name__:
                results.update({k: v})
        return results

    def new(self, obj):
        """Adds new object to storage dictionary
        Args:
            obj (BaseModel): object to add to storage"""
        if obj:
            self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def delete(self, obj=None):
        """This method deletes the object if it exists"""
        if obj is None:
            return
        key = obj.to_dict()['__class__'] + '.' + obj.id
        try:
            del FileStorage.__objects[key]
        except KeyError:
            pass
        FileStorage.save(self)
        pass

    def save(self):
        """Saves storage dictionary to file"""
        temp = {}
        temp.update(FileStorage.__objects)
        for key, val in temp.items():
            temp[key] = val.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def close(self):
        """This method calls reload() method for deserializing
        the JSON file to objects"""
        self.reload()
