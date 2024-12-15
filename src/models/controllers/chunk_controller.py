
from fastapi import APIRouter

router = APIRouter()

@router.get("/chunks")
def get_chunks():
    """Endpoint to get text chunks.
    
    Returns:
        dict: Placeholder response.
    """
    return {"message": "Chunks fetched successfully"}
