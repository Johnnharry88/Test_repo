#!/usr/bin/python3
"""Module that writes to MySQL database
using slqalchemy"""
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
import equi_model
from equi_model.gause import Gause
from equi_model.forcepts import Forcept
from equi_model.steth import Steth
from equi_model.syringes import Syringe
from equi_model.order import Order
from equi_model.city import City
from equi_model.state import State
from equi_model.user import User
from equi_model.base_model import BaseModel, Base

classes = {'User': User, 'Order': Order, 'State': State, 'City': City, 'Steth': Steth, 'Gause': Gause, 'Syringe': Syringe, 'Forcept': Forcept}


class EquiSQLstore:
    """Defines a variable for connecting and querying
    MySQL database"""
    connect = None
    search = None

    def __init__(self):
        user = getenv('USER')
        password = getenv('PASSWORD')
        database = getenv('DATABASE')
        host = getenv('HOST')
        env = getenv("EQUIMED_ENV")

        self.connect = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                    .format(user, password, host, database),
                                    pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.connect)

    def all(self, cls=None):
        """Return Dictionary of objects saved in table"""
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            res = self.search.query(cls)
            for x in res:
                key = "{}.{}".format(type(x).__name__, x.id)
                dic[key] = x
        else:
            for y in classes:
                res = self.search.query(classes[y]).all()
                for a in res:
                    key = "{}.{}".format(type(a).__name__, a.id)
                    dic[key] = a
        return (dic)

    def new(self, obj):
        """Adds a new element to database"""
        self.search.add(obj)

    def save(self):
        """Saves changes to database"""
        self.search.commit()

    def delete(self, obj=None):
        """Removes an element from the table"""
        if obj:
            self.search.delete(obj)

    def reload(self):
        """ loads existing data from database"""
        Base.metadata.create_all(self.connect)
        sec = sessionmaker(bind=self.connect, expire_on_commit=False)
        Session = scoped_session(sec)
        self.search = Session()

    def close(self):
        """Calls remove"""
        self.search.remove()

    def get(self, cls, id):
        """Returns obj based on the class name and its ID"""
        if cls not in classes.values():
            return None
        all_cls = equi_model.storage.all(cls)
        for x in all_cls.values():
            if (x.id == id):
                    return x
        return None

    def count(self, cls=None):
        """counts number of objects in storage"""
        all_clas = classes.values()
        if not cls:
            count = 0
            for x in all__clas:
                count = count + len(equi_model.storage.all(x).values())
        else:
            count = count + len(equi_model.storage.all(cls).values())
        return count
