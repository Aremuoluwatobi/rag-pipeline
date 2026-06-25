from vectordb import client
from embed import model
from log_config import logger


def retrieve_data(question, top_k=4, source_filter=None):

    try:
        collection = client.get_or_create_collection(name="rag_table")
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
        if source_filter:
            logger.info(
                f"Successfully retrieved {len(paired)} results for: {question[:50]} filtered by {source_filter}")
        else:
            logger.info(
                f"Successfully retrieved {len(paired)} results for: {question[:50]}")

        return paired
    except Exception as e:
        logger.error(f"Retrieval error: {e}")
        return None
