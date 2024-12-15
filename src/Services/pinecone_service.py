# Compliance_checker/src/services/pinecone_service.py
import pinecone
from configuration.config import Config

def initialize_pinecone():
    """Initialize Pinecone service.
    
    Returns:
        pinecone.Index: Pinecone index object.
    """
    pinecone.init(api_key=Config.PINECONE_API_KEY)
    index = pinecone.Index(Config.INDEX_NAME)
    return index
