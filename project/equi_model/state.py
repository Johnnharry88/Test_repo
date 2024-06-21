#!/usr/bin/python3
"""Module Defines State Class"""

from equi_model.base_model import BaseModel, Base
from equi_model.city import City
from os import getenv
#from equi_model import storage
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

#    def __init__(self, *arg, **kwarg):
#        """Initializes state"""
#        super().__init__(*arg, **kwarg)

    if datastore != "sql":
        @property
        def cities (self):
            """function for getting cities as related to state"""
            city_list = []
            all_city = storage.all(City)
            for city in all_city.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
