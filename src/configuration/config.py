
import os

class Config:
    EMBEDDING_FILE = os.getenv('EMBEDDING_FILE', 'path_to_your_embedding_file.pkl')
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY', 'your_pinecone_api_key')
    INDEX_NAME = os.getenv('INDEX_NAME', 'your_index_name')
