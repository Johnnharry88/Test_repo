#!/usr/bin/python3
"""This performs JSON storage"""
import json
import equi_model
from equi_model.base_model import BaseModel
from equi_model.user import User
from equi_model.state import State
from equi_model.city import City
from equi_model.order import Order
#from equi_model.gause import Gause
#from equi_model.steth import Steth
#from equi_model.forcepts import Forcept
#from equi_model.syringes import Syringe
import shlex


classes = {'User': User, 'Order': Order, "State": State, "City": City} #"Steth": Steth, "Forcept": Forcept, "Gause": Gause, "Syringe": Syringe}

class Store_Json:
    """Saves instances to JSON file and 
    loads JSON file to instance
    """
    path_json = "equi_med.json"
    equi_obj = {}

    def all(self, cls=None):
        """Returns a dictionary of a
        given class name
        """
        dic = {}
        if cls:
            x_store = self.equi_obj
            for key in x_store:
                div = key.replace('.', ' ')
                div_x = shlex.split(div)
                if (div_x[0] == cls.__name__):
                    dic[key] = self.equi_obj[key]
            return (dic)
        else:
            return self.equi_obj

    def new(self, obj):
        """sets in equi_obj obj with key<obj.name, obj.id>
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.equi_obj[key] = obj

    def save(self):
        """Saves obj to JSON file equi_med.json"""
        file_dict = {}
        for key, value in self.equi_obj.items():
            file_dict[key] = value.dict_pro()
        with open(self.path_json, 'w', encoding="utf-8") as f:
            json.dump(file_dict, f)

    def reload(self):
        """Loads file form Json file equi_med.json"""
        try:
            with open(self.path_json, 'r', encoding="utf-8") as f:
                for k, v in (json.load(f)).items():
                    v = eval(v["__class__"])(**v)
                    self.equi_obj[k] = v
        except FileNotFoundError:
            pass

    def delete(self, obj = None):
        """Removes an exisiting key/value pair
        preventing acess to dict in json file
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.equi_obj[key]

    def close(self):
        """Reloads self.equi_obj
        """
        self.relaod()

    def get(self, cls, id):
        """ Returns the object based on class name and id"""
        if cls not in classes.values():
            return None
        all_cls = equi_model.storage.all(cls)
        for x in all_cls.values():
            if (x.id == id):
                return x
        return None

    def count(slef, cls = None):
        """Counts number of objects in storage"""
        all_cls = classes.values()
        if not cls:
            count = 0
            for x in all_cls:
                count = count + len(equi_model.storage.all(x).values())
        else:
            count = count + len(equi_model.storage.all(cls).values())
        return count
