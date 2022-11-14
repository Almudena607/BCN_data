from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

client = MongoClient(os.getenv("url"))
db = client.get_database("BCN_data")

def get_data(collection, filter = {}, project = {"_id":0}, limit = 0, skip = 0):
    return db[collection].find(filter, project).limit(limit).skip(skip)