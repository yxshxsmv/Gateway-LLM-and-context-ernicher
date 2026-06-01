# retriever.py
# PURPOSE: Given a query, find the most relevant chunks from your documents

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_FOLDER = "./chroma_db"
EMBED_MODEL = "all-MiniLM-L6-v2"
TOP_K = 4  # How many chunks to retrieve per query

# Load the vector store once (reused across queries)
embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)
vectorstore = Chroma(
    persist_directory=CHROMA_FOLDER,
    embedding_function=embeddings
)

def retrieve_context(query: str) -> str:
    """
    Takes a plain-English query.
    Returns the most relevant text chunks from your documents as a single string.
    """
    docs = vectorstore.similarity_search(query, k=TOP_K)
    
    # Join the chunks into one block of context text
    context = "\n\n---\n\n".join([doc.page_content for doc in docs])
    return context


# Test it directly
if __name__ == "__main__":
    test_query = "What are our Q3 OKRs?"
    result = retrieve_context(test_query)
    print("Retrieved context:\n")
    print(result)