#!/usr/bin/env python3
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
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.now().isoformat())
                elif key == '__class__':
                    continue
                else:
                    setattr(self, key, value)
        
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    
    def __str__(self):
        """string method

        Returns:
            str: should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
    
    def save(self):
        """updates the public instance attribute,
                updated_at with the current datetime
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        cpy_dict = {}
        for key, value in self.__dict__.items():
            cpy_dict['__class__'] = self.__class__.__name__
            if key == 'created_at' or key == 'updated_at':
                cpy_dict[key] = str(datetime.now().isoformat())
            cpy_dict[key] = value
        
        return cpy_dict