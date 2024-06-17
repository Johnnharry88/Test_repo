#!/usr/bin/python3
from equi_model.base_model import BaseModel, Base
#from equi_model.__init__ import storage
from os import getenv
from sqlalchemy import Column, Integer, ForeignKey, String

datastore = getenv('DATASTORE')


class Steth(BaseModel, Base):
    """ class stethoscope"""
    if datastore == "sql":
        __tablename__ = "stethoscopes"
        order_id = Column(String(60), ForeignKey("orders.id"), nullable=False)
        quantity = Column(Integer, nullable=True)
        price = Column(String(60), nullable=True)
    else:
        order_id = ""
        quantity = ""
        price = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Steth"""
        super().__init__(*args, **kwargs)
