# Compliance_checker/src/model/controllers/embedding_controller.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/embeddings")
def get_embeddings():
    """Endpoint to get embeddings.
    
    Returns:
        dict: Placeholder response.
    """
    return {"message": "Embeddings fetched successfully"}
