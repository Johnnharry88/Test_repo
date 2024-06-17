#!/usr/bin/python3
"""Module of class Syringe"""
from equi_model.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer
#from equi_model.__init__ import storage

datastore = getenv('DATASTORE')


class Syringe(BaseModel, Base):
    """Module for Syringe"""
    if datastore == "sql":
        __tablename__ = "syringes"
        order_id = Column(String(60), ForeignKey("orders.id"), nullable=False)
        size = Column(Integer, nullable=False)
        quantity = Column(Integer, nullable=True)
        price = Column(String(60), nullable=True)

    else:
        order_id = ""
        size = ""
        quantity = ""
        price = ""

    def __init__(self, *args, **kwargs):
        """Initializing the Syringe module"""
        super().__init__(*args, **kwargs)
