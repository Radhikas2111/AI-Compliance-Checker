from fastapi import FastAPI
from models.controllers import (
    chunk_controller,
    embedding_controller,
    ingestion_controller,
    upload_controller
)

app = FastAPI()

app.include_router(chunk_controller.router, prefix="/chunks")
app.include_router(embedding_controller.router, prefix="/embeddings")
app.include_router(ingestion_controller.router, prefix="/ingest")
app.include_router(upload_controller.router, prefix="/upload")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
