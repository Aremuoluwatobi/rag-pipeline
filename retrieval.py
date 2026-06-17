from embed import model
from vectordb import collection


def retrieve_data(question, top_k=4, source_filter=None):

    try:
        query_embedding = model.encode([question])[0]

        query_params = {
            "query_embeddings": [query_embedding],
            "n_results": top_k
        }

        if source_filter:
            query_params["where"] = {"source": source_filter}

        result = collection.query(**query_params)

        docs = result["documents"][0]
        metadatas = result["metadatas"][0]

        paired = list(zip(docs, metadatas))

        return paired
    except Exception as e:
        print(f"Retrieval error: {e}")
        return None
