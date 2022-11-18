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

"""#returns the nationalities of the immigrants
@router.get("/immigrant/nation_list")
def distinct_nationality():
    res = db["Immigrants"].find({}).distinct("Nationality")
    return loads(json_util.dumps(res))
"""

# information of the immigrants in BCN depending on the neighborhood
@router.get("/neighborhood/immigrants/{neighborhood}")
def neig_immigrants(neighborhood: int, num_page: int = 0):
    res = find_collection("Immigrants", {"Neighborhood Code": neighborhood})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))


# information of the immigrants in BCN depending on the district
@router.get("/district/immigrants/{district}")
def district_immigrants(district: int, num_page: int = 0):
    res = find_collection("Immigrants", {"District Code": district})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))


# information of the immigrants in BCN depending on their nationality
@router.get("/nationality/immigrants/{nationality}")
def nationality_immigrants(nationality: str, num_page: int = 0):
    res = find_collection("Immigrants", {"Nationality": nationality})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))
