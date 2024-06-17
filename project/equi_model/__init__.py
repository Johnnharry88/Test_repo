#!/usr/bin/python3
from os import getenv
from equi_model.base_model import BaseModel, Base
from equi_model.user import User
from equi_model.order import Order
from equi_model.state import State
from equi_model.city import City
#from equi_model.steth import Steth
#from equi_model.gause import Gause
#from equi_model.syringes import Syringe
#from equi_model.forcepts import Forcept



from equi_model.engine.equi_sql import EquiSQLstore
storage = EquiSQLstore()

#from equi_model.engine.store_json import Store_Json
#storage = Store_Json()

storage.reload()
