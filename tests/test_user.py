#!/usr/bin/env python3
import unittest
from models.user import User
"""This is the test case for user module
"""


class TestCaseUser(unittest.TestCase):
    """This is the TestCaseUser class for test case of the User class,
        methods and attributes
    """
    def test_cls_attr(self):
        user_instance = User()

        self.assertTrue(hasattr(user_instance, 'email'))
        self.assertTrue(hasattr(user_instance, 'password'))
        self.assertTrue(hasattr(user_instance, 'first_name'))
        self.assertTrue(hasattr(user_instance, 'last_name'))


if __name__ == '__main__':
    unittest.main()
