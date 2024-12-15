
from fastapi import APIRouter, UploadFile, HTTPException
from models.managers.Upload_manager import UploadManager

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile):
    """Endpoint to upload a file.
    
    Args:
        file (UploadFile): The uploaded file object.
    
    Returns:
        dict: Response message with file path.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

    manager = UploadManager()
    saved_path = await manager.save_file(file)
    return {"message": "File successfully uploaded", "file_path": saved_path}
