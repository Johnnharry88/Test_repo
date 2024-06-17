#!/usr/bin/python3
"""Defnes Module Forcepts"""
from equi_model.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from os import getenv
#from equi_model.__init__ import storage

datastore = getenv('DATASTORE')


class Forcept(BaseModel, Base):
    """ class that defines forcepts"""
    if datastore == "sql":
        __tablename__ = "forcepts"
        order_id = Column(String(60), ForeignKey("orders.id"), nullable=False)
        quantity = Column(Integer, nullable=True)
        price = Column(String(60), nullable=True)

    else:
        order_id = ""
        quantity = ""
        price = ""

    def __init__(self, *args, **kwargs):
        """Initializes the Forcept"""
        super().__init__(*args, **kwargs)
