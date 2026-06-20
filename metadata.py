from vectordb import client


def get_available_pdfs():
    try:
        collection = client.get_or_create_collection(name="rag_table")
        results = collection.get()

        pdfs = set()
        for meta in results["metadatas"]:
            pdfs.add(meta["source"])

        return list(pdfs)
    except Exception as e:
        print(f"Pdf error: {e}")
        return []
