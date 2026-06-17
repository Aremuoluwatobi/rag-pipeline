import os
from pdf_reader import extract_all_text
from chunk import do_chunking
from embed import get_embeded
from vectordb import add_database


DOCUMENTS_FOLDER = "documents"


def ingest_pipeline():

    try:

        files = os.listdir(DOCUMENTS_FOLDER)

        for file in files:
            if not file.endswith((".pdf", ".docx")):
                continue

            file_path = os.path.join(DOCUMENTS_FOLDER, file)

            text = extract_all_text(file_path)
            if text is None:
                print(f"skipping {file}")
                continue

            chunks = do_chunking(text)
            if chunks is None:
                print(f"skipping {file}")
                continue

            embeddings = get_embeded(chunks)
            if embeddings is None:
                print(f"skipping {file}")
                continue

            add_database(
                chunks,
                embeddings,
                source_name=file
            )

        print("All documents ingested")

    except Exception as e:
        print(f"Ingestion Error: {e}")
