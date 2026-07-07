from petro_utils.vector_store import load_vector_store


def retrieve_context(vector_db, query, k=4):
    """
    Retrieve the most relevant chunks from the vector database.
    """

    docs = vector_db.similarity_search(query, k=k)

    context = "\n\n".join(doc.page_content for doc in docs)

    return context