from fastapi import  HTTPException, APIRouter
from database.mongodb import find_collection, paginate
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
def total_immigrants(neighborhood: str, num_page: int = 0):
    res = find_collection("Neighborhoods", {"_id": neighborhood}, {"Total Immigrants": 1})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))

@router.get("/totalunemployed/{neighborhood}")
def total_unemployed(neighborhood: str, num_page: int = 0):
    res = find_collection("Neighborhoods", {"_id": neighborhood}, {"Total Unemployed": 1})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))

@router.get("/totalpopulation/{neighborhood}")
def total_population(neighborhood: str, num_page: int = 0):
    res = find_collection("Neighborhoods", {"_id": neighborhood}, {"Total Population": 1})
    page = paginate(num_page)
    return loads(json_util.dumps(page(res)))