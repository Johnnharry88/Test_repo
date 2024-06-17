#!/usr/bin/python3
"""Module of class City"""
from equi_model.base_model import BaseModel, Base
from os import  getenv
from sqlalchemy import Column, String, ForeignKey
import sqlalchemy

datastore = getenv('DATASTORE')


class City(BaseModel, Base):
    """City Module"""
    if datastore == "sql":
        __tablename__ = "cities"
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(120), nullable=False)

    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """Initializes City"""
        super().__init__(*args, **kwargs)
