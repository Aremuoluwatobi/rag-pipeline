import chromadb
import uuid

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

        return "Documents stored successfully"

    except Exception as e:
        print(f"Vectordb Error: {e}")
        return False


def clear_database():
    global collection
    try:
        client.delete_collection("rag_table")
        collection = client.get_or_create_collection(name="rag_table")
        print("Database cleared")
    except Exception as e:
        print(f"Clear error: {e}")
