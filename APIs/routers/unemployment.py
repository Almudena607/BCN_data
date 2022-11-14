from fastapi import ApiRouter
from Database.mongodb import db
from bson import json_util
from json import loads

router = ApiRouter()

@router.get("/all/Unemployment")
def get_unemployment():
    res = get_data("Unemployment")
    return loads(json_util.dumps(res))