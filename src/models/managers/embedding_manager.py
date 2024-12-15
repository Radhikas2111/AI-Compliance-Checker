
from ETL.embeddings import create_embeddings

class EmbeddingManager:
    def create_embeddings(self, splits):
        """Create embeddings for text chunks.
        
        Args:
            splits (list): List of text chunks.
        
        Returns:
            list: List of embeddings.
        """
        embeddings = create_embeddings(splits)
        return embeddings
