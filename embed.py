from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embeded(chunks):
    try:
        embeddings = model.encode(chunks)

        return embeddings
    except Exception as e:
        print(f"Embedding Error: {e}")
        return None
