#!/usr/bin/env python3
import models
from datetime import datetime
from uuid import uuid4
"""This is the base_model module with one class - BaseModel
"""


class BaseModel:
    """This class defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Instanstiation method for the class with attributes:
            id, created_at and updated_at
        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, fmt)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """updates the public instance attribute,
                updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
                keys/values of __dict__ of the instance

        Returns:
            dict: dictionary of __dict__ of instance
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = datetime.now().isoformat()
        my_dict["updated_at"] = datetime.now().isoformat()
        
        return my_dict
    
    def __str__(self):
        """string method

        Returns:
            str: should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"