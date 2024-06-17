#!/usr/bin/python3
from equi_model.base_model import BaseModel, Base
from equi_model.steth import Steth
from equi_model.syringes import Syringe
from equi_model.gause import Gause
from equi_model.forcepts import Forcept
from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, Date, ForeignKey
#from equi_model.__init__ import storage
from sqlalchemy.orm import relationship
import sqlalchemy
from equi_model.city import City


datastore = getenv('DATASTORE')


class Order(BaseModel, Base):
    """Defines the attributes of Order"""
    if datastore == "sql":
        __tablename__ = "orders"
        _date = Column(Date, default = datetime.today(), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        contact_address = Column(String(128), nullable=True)
        del_phone = Column(String(120), nullable=False)
        cities_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        gause = relationship("Gause", cascade="all, delete, delete-orphan",                                    backref="order")
        forcept = relationship("Forcept", cascade="all, delete, delete-orphan",                                backref="order")
        stethoscope = relationship("Steth", cascade="all, delete, delete-orphan",                               backref="order")
        syringe = relationship("Syringe", cascade="all, delete, delete-orphan",                                 backref="order")
    else:
        user_id = ""
        cities_id = ""
        contact_address = ""
        del_phone = ""
        _date = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
