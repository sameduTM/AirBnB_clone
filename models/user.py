#!/usr/bin/env python3
from models.base_model import BaseModel
"""This is a user module that inherits from BaseModel
"""


class User(BaseModel):
    """This is the User class of the user
    module that inherits from the base model

    Args:
        BaseModel (Parent): User class inherits from this module
    """
    email = ""
    password = ""
    firstname = ""
    lastname = ""
