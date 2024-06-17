#!/usr/bin/python3
from os import getenv


datastore = getenv('DATASTORE')


if datastore == "sql":
    from equi_model.engine.equi_sql import EquiSQLstore
    storage = EquiSQLstore()
else:
    from equi_model.engine.store_json import Store_Json
    storage = Store_Json()

storage.reload()
