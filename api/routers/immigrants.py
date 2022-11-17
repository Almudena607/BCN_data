from fastapi import  HTTPException, APIRouter
from database.mongodb import find_collection, paginate


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

@router.get("/neighborhood/immigrants/{neighborhood}")
def neig_immigrants(neigborhood: int):
    res = find_collection("Immigrants", {"Neighborhood Code": neigborhood})
    return res


# information of the immigrants in BCN depending on the district

@router.get("/immigrants/{district}")
def district_immigrants(district: int):
    res = find_collection("Immigrants", {"District Code": district})
    return res

"""@router.get("/immigrants/{district}")
def district_immigrants(district:int):
    filt = {"District Code": district}
    total = list(db["Immigrants"].find(filt, {}))
    return loads(json_util.dumps(total))"""



# information of the immigrants in BCN depending on their nationality

@router.get("/immigrants/{nationality}")
def nationality_immigrants(nationality: str):
    res = find_collection("Immigrants", {"Nationality": nationality})
    return get_immigrants(res)


# filter depending on the year of the data
@router.get("/immigrants/{year}/{neigborhood}")
def year_neig(year: int, neigborhood: str):
    res = find_collection("Immigrants", {
        "$and":
        [{"Year": year}, 
        {"Neighborhood Name": neigborhood}]})
    return get_immigrants(res)

@router.get("/immigrants/{year}/{district}")
def year_district(year: int, district: str):
    res = find_collection("Immigrants", 
        {"$and":
        [{"Year": year}, 
        {"District Name": district}]})
    return get_immigrants(res)


@router.get("/immigrants/{year}/{nationality}")
def year_nationality(year: int, nationality: str):
    res = find_collection("Immigrants", 
        {"$and":
        [{"Year": year}, 
        {"Nationality": nationality}]})
    return get_immigrants(res)
