from fastapi import APIRouter
from database.mongodb import find_collection, paginate
from bson import json_util
from json import loads

router = APIRouter()


@router.get("/unemployment")
def get_unemployment(num_page: int = 0):
    print(f"Fetching page {num_page}")

    # Validate page number

    if num_page < 0:
        raise HTTPException(
            status_code=400, detail="num_page must be a positive integer")

    # Configure paginator with query parameters
    page = paginate(num_page)

    # Fetch page data
    res = page(find_collection("Unemployment"))
    return res


# information of the unemployment in BCN depending on the neighborhood
@router.get("/neighborhood/unemployment/{neighborhood}")
def neig_unemployment(neighborhood: str, num_page: int = 0):
    res = find_collection("Unemployment", {"Neighborhood Name": neighborhood})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))


# information of the unemployment in BCN depending on the district
@router.get("/district/unemployment/{district}/{num_page}")
def district_unemployment(district: str, num_page: int = 0):
    res = find_collection("Unemployment", {"District Name": district, "Year": 2017})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))


# information of the unemployment in BCN depending on their gender
@router.get("/gender/unemployment/{gender}")
def gender_unemployment(gender: str, num_page: int = 0):
    res = find_collection("Unemployment", {"Gender": gender})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))

# information of the unemployment in BCN depending on the demand occupation
@router.get("/demand_occupation/unemployment/{demand_occupation}")
def occupation_unemployment(demand_occupation: str, num_page: int = 0):
    res = find_collection("Unemployment", {"Demand_occupation": demand_occupation})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))

