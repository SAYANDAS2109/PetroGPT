from langchain.text_splitter import RecursiveCharacterTextSplitter


def split_text(text):
    """
    Split extracted PDF text into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )

    chunks = splitter.split_text(text)

    return chunks
