import os
from pymongo import MongoClient
DATABASE_URI = os.environ.get('DATABASE_URI',"default_value") 
cluster = MongoClient(DATABASE_URI)

db = cluster.ecesite
