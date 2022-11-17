from fastapi import  HTTPException, APIRouter
from database.mongodb import find_collection, paginate


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