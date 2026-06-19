from functools import lru_cache
from sentence_transformers import SentenceTransformer


@lru_cache(maxsize=1)
def get_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


model = get_model()


def get_embeded(chunks):
    try:
        embeddings = model.encode(chunks)

        return embeddings
    except Exception as e:
        print(f"Embedding Error: {e}")
        return None
