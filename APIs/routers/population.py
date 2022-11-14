from fastapi import APIRouter
from Database.mongodb import db
from bson import json_util
from json import loads

router = APIRouter()

#este router devuelve la info de las primeras filas de población
@router.get("/all/Population")
def get_population():
    res = list(db["Population"].find({}))[5]
    return loads(json_util.dumps(res))