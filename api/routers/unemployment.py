from fastapi import APIRouter
from database.mongodb import find_collection, paginate


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

@router.get("/unemployment/{neighborhood}")
def neig_unemployment(neigborhood = str):
    res = find_collection("Unemployment", {"Neighborhood Name": neigborhood})
    return get_unemployment(res)


# information of the unemployment in BCN depending on the district

@router.get("/unemployment/{district}")
def district_unemployment(district = str):
    res = find_collection("Unemployment", {"District Name": district})
    return get_unemployment(res)


# information of the unemployment in BCN depending on their gender

@router.get("/unemployment/{gender}")
def gender_unemployment(gender = str):
    res = find_collection("Unemployment", {"Gender": gender})
    return get_unemployment(res)

# information of the unemployment in BCN depending on the demand occupation

@router.get("/unemployment/{demand_occupation}")
def occupation_unemployment(demand_occupation = str):
    res = find_collection("Unemployment", {"Demand_occupation": demand_occupation})
    return get_unemployment(res)


# filter depending on the year and the month of the data

@router.get("/unemployment/{year}/{month}")
def year_month(year = int, month = str):
    res = find_collection("Unemployment", 
        {"$and":
        [{"Year": year}, 
        {"Month": month}]})
    return get_unemployment(res)

