#!/usr/bin/env python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from uuid import UUID
"""This is the test module for the BaseModel class
"""


class TestBaseModel(unittest.TestCase):
    """This is the test case for BaseModel class
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_instance_attributes(self):
        """Test if the instance has the expected attributes
        """
        model_instance = BaseModel()
        self.assertTrue(hasattr(model_instance, 'id'))
        self.assertTrue(hasattr(model_instance, 'created_at'))
        self.assertTrue(hasattr(model_instance, 'updated_at'))
        self.assertIsInstance(model_instance.id, str)
        self.assertIsInstance(model_instance.created_at, datetime)
        self.assertIsInstance(model_instance.updated_at, datetime)

    def test_id_is_uuid(self):
        """Test if id is a valid UUID
        """
        model_instance = BaseModel()
        self.assertIsInstance(UUID(model_instance.id, version=4), UUID)

    def test_created_at_update_at(self):
        """Test if created_at and updated_at are datetime objects
        """
        model_instance = BaseModel()
        self.assertIsInstance(model_instance.created_at, datetime)
        self.assertIsInstance(model_instance.updated_at, datetime)

    def test_updated_at_after_save(self):
        """Test if updated_at changes after saving the instance
        """
        model_instance = BaseModel()
        old_update = model_instance.updated_at
        model_instance.save()
        self.assertNotEqual(old_update, model_instance.updated_at)

    def test_init_with_dict(self):
        """Test if initializing with a dictionary
            sets attributes correctly
        """
        mdl_dict = {
            'id': 'some_id',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-02T12:30:00.000000'
        }
        mdl_inst = BaseModel(**mdl_dict)

        self.assertEqual(mdl_inst.id, mdl_dict['id'])
        self.assertEqual(mdl_inst.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
                         mdl_dict['created_at'])
        self.assertEqual(mdl_inst.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
                         mdl_dict['updated_at'])

        """def test_to_dict(self):
        # Test if to_dict method returns the expected dictionary
        mdl_inst = BaseModel()
        mdl_dict = mdl_inst.to_dict()

        self.assertIsInstance(mdl_dict, dict)
        self.assertEqual(mdl_dict['id'], mdl_inst.id)
        self.assertEqual(mdl_dict['created_at'],
                         mdl_inst.created_at.isoformat())
        self.assertEqual(mdl_dict['updated_at'],
                         mdl_inst.updated_at.isoformat())"""


if __name__ == '__main__':
    unittest.main()
