from fastapi import  HTTPException, APIRouter
from database.mongodb import db, find_collection, paginate
from bson import json_util
from json import loads

router = APIRouter()


# https://fastapi.tiangolo.com/tutorial/query-params/?h=query+pa


@router.get("/immigrants")
def get_immigrants(num_page: int = 0):
    print(f"Fetching page {num_page}")

    # Validate page number

    if num_page < 0:
        raise HTTPException(
            status_code=400, detail="num_page must be a positive integer")

    # Configure paginator with query parameters
    page = paginate(num_page)

    # Fetch page data
    res = page(find_collection("Immigrants"))
    return res


# information of the immigrants in BCN depending on the neighborhood
@router.get("/neighborhood/immigrants/{neighborhood}/{num_page}")
def neig_immigrants(neighborhood: str, num_page: int = 0):
    res = find_collection("Immigrants", {"Neighborhood Name": neighborhood, "Year": 2017})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))


# information of the immigrants in BCN depending on the district
@router.get("/district/immigrants/{district}/{num_page}")
def district_immigrants(district: str, num_page: int=0):
    res = find_collection("Immigrants", {"District Name": district, "Year": 2017})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))


# information of the immigrants in BCN depending on their nationality
@router.get("/nationality/immigrants/{nationality}/{num_page}")
def nationality_immigrants(nationality: str, num_page: int = 0):
    res = find_collection("Immigrants", {"Nationality": nationality, "Year": 2017})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))


# muestra el nombre de todas las nacionalidades
@router.get("/nationality/all")
def distinct_nationality():
    res = db["Immigrants"].find({"Year": 2017}).distinct("Nationality")
    return loads(json_util.dumps(res))


# muestra el nombre de todas los distritos
@router.get("/district/all")
def distinct_district():
    res = db["Immigrants"].find({"Year": 2017}).distinct("District Name")
    return loads(json_util.dumps(res))
