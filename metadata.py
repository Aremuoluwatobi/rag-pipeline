from vectordb import collection


def get_available_pdfs():
    try:
        results = collection.get()

        pdfs = set()
        for meta in results["metadatas"]:
            pdfs.add(meta["source"])

        return list(pdfs)
    except Exception as e:
        print(f"Pdf error: {e}")
        return None
