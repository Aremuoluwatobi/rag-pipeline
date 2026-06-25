from vectordb import client
from log_config import logger


def get_available_pdfs():
    try:
        collection = client.get_or_create_collection(name="rag_table")
        results = collection.get()

        pdfs = set()
        for meta in results["metadatas"]:
            pdfs.add(meta["source"])

        logger.info(f"Found {len(pdfs)} Pdf's available")
        return list(pdfs)
    except Exception as e:
        logger.error(f"Pdf error: {e}")
        return []
