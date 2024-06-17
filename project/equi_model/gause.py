#!/usr/bin/python3
from equi_model.base_model import BaseModel, Base
#from equi_model.__init__ import storage
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer

datastore = getenv('DATASTORE')


class Gause(BaseModel, Base):
    """Fefines Gause attributes"""
    if datastore == "sql":
        __tablename__ = "gause"
        order_id = Column(String(60), ForeignKey("orders.id"), nullable=False)
        quantity = Column(Integer, nullable=True)
        price = Column(String(60), nullable=True)
    else:
        order_id = ""
        quantity = ""
        price = ""

    def __init__(self, *args, **kwargs):
        """Initialize the Gause """
        super().__init__(*args, **kwargs)

