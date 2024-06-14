#!/usr/bin/python3
"""Module of class Syringe"""
from equi_model.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer
#from equi_model.__init__ import storage


class Syringe(BaseModel, Base):
    """Module for Syringe"""
    __tablename__ = "syringes"
    order_id = Column(String(60), ForeignKey("orders.id"), nullable=False)
    size = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=True)
    price = Column(String(60), nullable=True)

    def __init__(self, *args, **kwargs):
        """Initializing the Syringe module"""
        super().__init__(*args, **kwargs)
