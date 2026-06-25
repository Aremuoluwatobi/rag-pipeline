from functools import lru_cache
from sentence_transformers import SentenceTransformer
from log_config import logger


@lru_cache(maxsize=1)
def get_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


model = get_model()


def get_embeded(chunks):
    try:
        embeddings = model.encode(chunks)
        logger.info(f"Successfully embeded {len(chunks)} chunks")

        return embeddings
    except Exception as e:
        logger.error(f"Embedding Error: {e}")
        return None
