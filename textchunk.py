from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)


def do_chunking(text):

    try:
        chunk = splitter.split_text(text)

        return chunk
    except Exception as e:
        print(f"Chunking Error: {e}")
        return None
