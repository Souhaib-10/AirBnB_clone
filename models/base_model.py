#!/usr/bin/python3
'''a module BaseModel that define base class for create all other classes'''
import uuid
from datetime import datetime


class BaseModel:
    '''a class BaseModel that defines all common attr/meth for other classes'''
    def __init__(self, *args, **kwargs):
        '''
        Initialize a new instance of BaseModels
        Args:
            *args: list of arguments
            **kwargs: list of key-values arguments
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f'
                                )
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        '''display information about instante class'''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''change  time when update some record'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns a dictionary containing all keys/values'''
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
