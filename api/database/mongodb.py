from pymongo import MongoClient
from bson import json_util
from json import loads
from config import DBURL

client = MongoClient(DBURL)
db = client.get_database("BCN_data")


def find_collection(collection, filter={}, project={"_id": 0}):
    return db[collection].find(filter, project)


def paginate(page=0, per_page=10):
    def inner(mongodb_cursor):
        data = mongodb_cursor.limit(per_page).skip(per_page*page)
        return {
            "page": page,
            "results": loads(json_util.dumps(data))
        }
    return inner
