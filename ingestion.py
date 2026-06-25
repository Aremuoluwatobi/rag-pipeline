import os
from log_config import logger
from huggingface_hub import snapshot_download
from pdf_reader import extract_all_text
from textchunk import do_chunking
from embed import get_embeded
from vectordb import add_database


DOCUMENTS_FOLDER = "documents"


def download_documents():
    snapshot_download(
        repo_id="AremuTaiwo/rag-documents",
        repo_type="dataset",
        local_dir="documents"
    )


def ingest_pipeline():

    try:

        files = os.listdir(DOCUMENTS_FOLDER)

        for file in files:
            if not file.endswith((".pdf", ".docx")):
                continue

            file_path = os.path.join(DOCUMENTS_FOLDER, file)

            text = extract_all_text(file_path)
            if text is None:
                logger.warning(f"Skipping {file} — text extraction failed")
                continue

            chunks = do_chunking(text)
            if chunks is None:
                logger.warning(f"Skipping {file} — chunking failed")
                continue

            embeddings = get_embeded(chunks)
            if embeddings is None:
                logger.warning(f"Skipping {file} — embedding failed")
                continue

            add_database(
                chunks,
                embeddings,
                source_name=file
            )

        logger.info("All documents ingested successfully")

    except Exception as e:
        logger.error(f"Ingestion Error: {e}")
