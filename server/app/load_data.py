from pymongo import MongoClient
db_client = MongoClient('mongodb://db:27017/')
print(db_client.server_info())


mydb = db_client["user_data"]
mycol = mydb["data"]

import csv
import uuid
import pandas as pd
import numpy as np
mongoResponse = mycol.delete_many({})
mongoResponse = mycol.insert_many(user_data)
# check methods to do pymongo operations
