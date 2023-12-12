#!/usr/bin/env python3
import unittest
from models.state import State
"""This is the test case for the state module
"""


class TestState(unittest.TestCase):
    """This class runs test case for the state module
    """
    def test_cls_attr(self):
        """This function tests the public attributes of the State class
        """
        state_instance = State()
        self.assertEqual(state_instance.name, "")
