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
    res = page(db["Population"].find({"Year": 2017}))
    return res


# information of the population in BCN depending on the district
@router.get("/district/population/{district}/{num_page}")
def district_population(district: str, num_page: int = 0):
    res = find_collection("Population", {"District.Name": district, "Year": 2017})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))


