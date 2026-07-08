from petro_utils.vector_store import load_vector_store


def retrieve_context(vector_db, query):
    retriever = vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,
            "fetch_k": 15
        }
    )

    docs = retriever.invoke(query)

    context = "\n\n".join(doc.page_content for doc in docs)

    return context
