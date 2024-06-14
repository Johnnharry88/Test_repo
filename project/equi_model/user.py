#!/usr/bin/python3
from equi_model.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from equi_model.order import Order
from hashlib import md5

datastore = getenv("EQUIMED_TYPE_STORAGE")


class User(BaseModel, Base):
    """Represents a User """
    if datastore == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=True)
        address = Column(String(128), nullable=False)
        phone_no = Column(String(64), nullable=False)
        gender = Column(String, nullable=True)
        orders = relationship("Order", cascade='all, delete, delete-orphan',
                            backref="user")
    else:
        first_name = ""
        last_name = ""
        email = ""
        password = ""
        phone_no = ""
        gender = ""
        address = ""
        state = ""
        city = ""

    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """Encrypts the password with nd5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
