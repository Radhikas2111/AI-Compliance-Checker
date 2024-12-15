# Compliance_checker/src/model/managers/chunk_manager.py
from ETL.text_chunking import split_document

class ChunkManager:
    def chunk_file(self, docs):
        """Chunk the extracted text from the documents.
        
        Args:
            docs (list): List of documents to be chunked.
        
        Returns:
            list: List of text chunks.
        """
        splits = split_document(docs)
        return splits
