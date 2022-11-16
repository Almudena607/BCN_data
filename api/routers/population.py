from fastapi import APIRouter
from database.mongodb import find_collection, paginate


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
@router.get("/population/{neighborhood}")
def neig_population(neigborhood = str):
    res = find_collection("Population", {"Neighborhood.Name": neigborhood})
    return get_population(res)


# information of the population in BCN depending on the district
@router.get("/population/{district}")
def district_population(district = str):
    res = find_collection("Population", {"District.Name": district})
    return get_population(res)


# the information of the population in BCN depending on their gender
@router.get("/population/{gender}")
def gender_population(gender = str):
    res = find_collection("Population", {"Gender": gender})
    return get_population(res)


# information of the population in BCN depending on their age
@router.get("/population/{age}")
def age_population(age = int):
    res = find_collection("Population", {"Age": age})
    return get_population(res)


# filter depending on the year of the data
@router.get("/population/{year}/{neigborhood}")
def year_neig(year = int, neigborhood = str):
    res = find_collection("Population", {
        "$and":
        [{"Year": year}, 
        {"Neighborhood.Name": neigborhood}]})
    return get_population(res)

@router.get("/population/{year}/{district}")
def year_district(year = int, district = str):
    res = find_collection("Population", 
        {"$and":
        [{"Year": year}, 
        {"District.Name": district}]})
    return get_population(res)


@router.get("/population/{year}/{gender}")
def year_gender(year = int, gender = str):
    res = find_collection("Population", 
        {"$and":
        [{"Year": year}, 
        {"Gender": gender}]})
    return get_population(res)


@router.get("/population/{year}/{age}")
def year_age(year = int, age = int):
    res = find_collection("Population", 
        {"$and":
        [{"Year": year}, 
        {"Age": age}]})
    return get_population(res)