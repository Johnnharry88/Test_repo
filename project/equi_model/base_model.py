#!/usr/bin/python3
"""Module that holds a general attribute for other class
"""
import equi_model 
import uuid
from datetime import datetime
from sqlalchemy import Column, String, Date
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
import json

datastore = getenv('DATASTORE')

if datastore == "sql":
    Base = declarative_base()
else:
    class Base:
        pass


class BaseModel:
    """Class that defines common attributes
    and method for class inheritance
    """
    if datastore == "sql":
        id = Column(String(60), primary_key=True)
        created_at = Column(Date, nullable=False, default=datetime.utcnow())
        updated_at = Column(Date, nullable=False, default=datetime.utcnow())

    def __init__(self, *arg, **kwarg):
        """Constructor that instiantiates object
        using its attributes
        """
        if kwarg:
            for k, v in kwarg.items():
                if k ==  "created_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

            if "id" not in kwarg:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwarg:
                self.crreated_at = datetime.now()
            if "updated_at" not in kwarg:
                self.updated_at = datetime.now()

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String Representation of instance
        """
        return "[{}] ({}) {}". format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates changes using the current date and time
        and saves it to Json file"""
        self.updated_at = datetime.now()
        equi_model.storage.new(self)
        equi_model.storage.save()
  
    def dict_pro(self):
        """return a dictionary containing all 
        keys/values of __dict__ of instance
        """
        dict_x = dict(self.__dict__)
        dict_x['__class__'] = str(type(self).__name__)
        dict_x['created_at'] = self.created_at.isoformat()
        dict_x['updated_at'] = self.updated_at.isoformat()
        if "-sa_instance_state" in dict_x.keys():
            del dict_x["_sa_instance_state"]
        return dict_x
