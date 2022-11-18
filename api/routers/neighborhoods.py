from fastapi import  HTTPException, APIRouter
from database.mongodb import db, find_collection, paginate
from bson import json_util
from json import loads

router = APIRouter()


@router.get("/neighborhoods")
def get_neighborhoods(num_page: int = 0):
    print(f"Fetching page {num_page}")

    # Validate page number

    if num_page < 0:
        raise HTTPException(
            status_code=400, detail="num_page must be a positive integer")

    # Configure paginator with query parameters
    page = paginate(num_page)

    # Fetch page data
    res = page(find_collection("Neighborhoods"))
    return res


@router.get("/totalimmigrants/{neighborhood}")
def total_immigrants(neighborhood: str):
    res = find_collection("Neighborhoods", {"_id": neighborhood}, {"Total Immigrants": 1})
    return loads(json_util.dumps(res))

@router.get("/totalunemployed/{neighborhood}")
def total_unemployed(neighborhood: str):
    res = find_collection("Neighborhoods", {"_id": neighborhood}, {"Total Unemployed": 1})
    return loads(json_util.dumps(res))

@router.get("/totalpopulation/{neighborhood}")
def total_population(neighborhood: str):
    res = find_collection("Neighborhoods", {"_id": neighborhood}, {"Total Population": 1})
    return loads(json_util.dumps(res))

#muestra el nombre de cada uno de los barrios
@router.get("/neighborhood/all")
def distinct_neighborhood():
    res = db["Neighborhoods"].find({}).distinct("_id")
    return loads(json_util.dumps(res))
