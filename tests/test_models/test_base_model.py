#!/usr/bin/python3
''' define unittests for base_model.py.'''
import unittest
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    ''' unittest for all functionality of  BaseModel class.'''

    def test_constructor(self):
        '''test instance'''
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_str_method(self):
        '''test str method'''
        model = BaseModel()
        model.id = "1234-5678-uuid"
        str_exp = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), str_exp)

    def test_save_method(self):
        '''test save method'''
        model = BaseModel()
        initial_update = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, initial_update)

    def test_to_dict_method(self):
        '''test to_dict method'''
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_instance_from_dict(self):
        '''test instance creation modek from model dictionary representation'''
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()
        print("to_dict")
        print(my_model_dict)
        my_new_model = BaseModel(**my_model_dict)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)

if __name__ == "__main__":
    unittest.main()
