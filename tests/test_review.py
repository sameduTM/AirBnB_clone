#!/usr/bin/env python3
import unittest
from models.review import Review
"""This is the test case module for review module"""


class TestReview(unittest.TestCase):
    """This class has test case funtions for the
        Review class - review module"""
    def test_review(self):
        """This method tests the existence of class attributes"""
        review_instance = Review()
        self.assertTrue(hasattr(review_instance, 'place_id'))
        self.assertTrue(hasattr(review_instance, 'user_id'))
        self.assertTrue(hasattr(review_instance, 'text'))
        self.assertTrue(isinstance(review_instance.place_id, str))


if __name__ == '__main__':
    unittest.main()
