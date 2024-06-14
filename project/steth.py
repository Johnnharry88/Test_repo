#!/usr/bin/python3
from equi_model.base_model import BaseModel, Base
#from equi_model.__init__ import storage
from os import getenv
from sqlalchemy import Column, Integer, ForeignKey, String


class Steth(BaseModel, Base):
    """ class stethoscope"""
    __tablename__ = "stethoscopes"
    order_id = Column(String(60), ForeignKey("orders.id"), nullable=False)
    quantity = Column(Integer, nullable=True)
    price = Column(String(60), nullable=True)

    def __init__(self, *args, **kwargs):
        """Initializes the Steth"""
        super().__init__(*args, **kwargs)
