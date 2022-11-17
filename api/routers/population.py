from fastapi import APIRouter
from database.mongodb import find_collection, paginate
from bson import json_util
from json import loads

router = APIRouter()

# information about the population in BCN

@router.get("/population")
def get_population(num_page: int = 0):
    print(f"Fetching page {num_page}")

    # Validate page number
    if num_page < 0:
        raise HTTPException(
            status_code=400, detail="num_page must be a positive integer")

    # Configure paginator with query parameters
    page = paginate(num_page)

    # Fetch page data
    res = page(db["Population"].find({}))
    return res


# information of the population in BCN depending on the neighborhood
@router.get("/neighborhood/population/{neighborhood}")
def neig_population(neighborhood: int, num_page: int = 0):
    res = find_collection("Population", {"Neighborhood.Code": neighborhood})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))


# information of the population in BCN depending on the district
@router.get("/district/population/{district}")
def district_population(district: int, num_page: int = 0):
    res = find_collection("Population", {"District.Code": district})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))

# the information of the population in BCN depending on their gender
@router.get("/gender/population/{gender}")
def gender_population(gender: str, num_page: int = 0):
    res = find_collection("Population", {"Gender": gender})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))


# information of the population in BCN depending on their age
@router.get("/age/population/{age}")
def age_population(age: int, num_page: int = 0):
    res = find_collection("Population", {"Age": age})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))

