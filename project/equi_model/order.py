#!/usr/bin/python3
from equi_model.base_model import BaseModel, Base
#from equi_model.syringes import Syringe
#from equi_model.steth import Steth
#from equi_model.forcepts import Forcept
#from equi_model.gause import Gause
from datetime import datetime
from os import getenv
from sqlalchemy import Column, String, Date, ForeignKey
#from equi_model.__init__ import storage
from sqlalchemy.orm import relationship

datastore = getenv('EQUIMED_TYPE_STORAGE')


class Order(BaseModel, Base):
    """Defines the attributes of Order"""
    if datastore == "db":
        __tablename__ = "orders"
        # order_date = Column(Date, default = datetime.today(), nullabl=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        delivery_address = Column(String(128), nullable=True)
        delivery_phone_no = Column(String(120), nullable=False)
        cities_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
#    gause = relationship("Gause", cascade="all, delete, delete-orphan",                                    backref="order")
#    forcept = relationship("Forcept", cascade="all, delete, delete-orphan",                                backref="order")
#    stethoscope = relationship("Steth", cascade="all, delete, delete-orphan",                               backref="order")
#    syringe = relationship("Syringe", cascade="all, delete, delete-orphan",                                 backref="order")
    else:
        user_id = ""
        cities_id = ""
        delivery_phone_no = ""
        delivery_address = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
