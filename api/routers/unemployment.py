from fastapi import APIRouter
from database.mongodb import db


router = APIRouter()

# @router.get("/all/Unemployment")
# def get_unemployment():
#     res = get_data("Unemployment")
#     return loads(json_util.dumps(res))
