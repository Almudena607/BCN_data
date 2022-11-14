from fastapi import ApiRouter
from Database.mongodb import db
from bson import json_util
from json import loads

router = ApiRouter()

#este router devuelve la info de los 5 primeros migrantes
@router.get("/all/Immigrants")
def get_immigrants():
    res = get_data("Immigrants")
    return loads(json_util.dumps(res))