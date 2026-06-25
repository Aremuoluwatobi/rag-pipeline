from langchain_text_splitters import RecursiveCharacterTextSplitter
from log_config import logger

splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)


def do_chunking(text):

    try:
        chunk = splitter.split_text(text)
        logger.info(f"Text split into {len(chunk)} chunks")

        return chunk
    except Exception as e:
        logger.error(f"Chunking Error: {e}")
        return None
