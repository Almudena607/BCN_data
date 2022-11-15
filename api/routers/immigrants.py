from fastapi import FastAPI, HTTPException, APIRouter
from database.mongodb import find_collection, paginate

router = APIRouter()

# este router devuelve la info de los 5 primeros migrantes

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
