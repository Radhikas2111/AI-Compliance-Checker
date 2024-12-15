
import os
from fastapi import UploadFile

class UploadManager:
    def __init__(self, upload_dir: str = "./uploaded_files"):
        """
        Initialize the UploadManager with an upload directory.
        
        Args:
            upload_dir (str): Directory where files will be uploaded.
        """
        self.upload_dir = upload_dir
        os.makedirs(self.upload_dir, exist_ok=True)
    
    async def save_file(self, file: UploadFile) -> str:
        """
        Save the uploaded file to the server.
        
        Args:
            file (UploadFile): The uploaded file object.
        
        Returns:
            str: Path where the file is saved.
        """
        file_path = os.path.join(self.upload_dir, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        return file_path
