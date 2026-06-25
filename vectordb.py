import chromadb
import uuid
from log_config import logger

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="rag_table")


def add_database(chunks, embeddings, source_name="unknown.pdf"):

    try:
        ids = [str(uuid.uuid4()) for _ in chunks]

        metadatas = [
            {"source": source_name} for _ in chunks
        ]

        collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )
        logger.info(
            f"successfully stored {len(chunks)} chunks from {source_name}")
        return True

    except Exception as e:
        logger.error(f"Vectordb Error: {e}")
        return False


def clear_database():
    global collection
    try:
        client.delete_collection("rag_table")
        collection = client.get_or_create_collection(name="rag_table")
        logger.info("Database cleared")
        return True
    except Exception as e:
        logger.error(f"Clear error: {e}")
        return False
