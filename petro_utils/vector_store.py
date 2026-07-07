from langchain_community.vectorstores import FAISS
from petro_utils.embeddings import embedding_model
import os

DB_PATH = "vector_db"


def create_vector_store(chunks):

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embedding_model
    )

    vector_store.save_local(DB_PATH)

    return vector_store


def load_vector_store():

    faiss_file = os.path.join(DB_PATH, "index.faiss")
    pkl_file = os.path.join(DB_PATH, "index.pkl")

    # No saved database yet
    if not (os.path.exists(faiss_file) and os.path.exists(pkl_file)):
        return None

    return FAISS.load_local(
        DB_PATH,
        embedding_model,
        allow_dangerous_deserialization=True
    )

    return vector_store
# from langchain_community.vectorstores import FAISS
# from petro_utils.embeddings import embedding_model

# def create_vector_store(chunks):
#     """
#     Creates a FAISS vector database from text chunks.

#     Args:
#         chunks (list): List of text chunks.

#     Returns:
#         FAISS: Vector database.
#     """

#     vector_db = FAISS.from_texts(
#         texts=chunks,
#         embedding=embedding_model
#     )
#     return vector_db

# def search_vector_store(vector_db,query,k=4):
#     """
#     Searches the vector database.

#     Args:
#         vector_db: FAISS database
#         query (str): User question
#         k (int): Number of relevant chunks

#     Returns:
#         list
#     """

#     docs = vector_db.similarity_search(
#         query,
#         k=k
#     )
#     return docs