from fastapi import APIRouter
from database.mongodb import db, get_data
from bson import json_util
from json import loads

router = APIRouter()

#este router devuelve la info de las primeras filas de población
@router.get("/all/Population")
def get_population():
    res = get_data("Population")
    return loads(json_util.dumps(res))