#!/usr/bin/python3
"""Module Defines State Class"""

from equi_model.base_model import BaseModel, Base
from equi_model.city import City
from os import getenv
#from equi_model.__init__ import storage
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

datastore = getenv('DATASTORE')


class State(BaseModel, Base):
    """This class describes the State attributes
    Attributes:
    name: State mane
    """
    if datastore == "sql":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                cascade="all, delete, delete-orphan")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initializes state"""
        super().__init__(*args, **kwargs)
