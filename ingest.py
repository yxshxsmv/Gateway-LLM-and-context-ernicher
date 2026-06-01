# ingest.py
# PURPOSE: Read all documents in /docs and build a Chroma vector database
# Run this once whenever you add new documents: python ingest.py

import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# --- CONFIG ---
DOCS_FOLDER = "./docs"          # Put your PDFs here
CHROMA_FOLDER = "./chroma_db"   # Where the vector DB is saved
EMBED_MODEL = "all-MiniLM-L6-v2"  # Small, fast, free embedding model
CHUNK_SIZE = 500                # How many characters per chunk
CHUNK_OVERLAP = 50              # Overlap between chunks (helps preserve context)

def ingest_documents():
    print("Loading documents from ./docs ...")
    
    # Load all PDFs from the docs folder
    loader = PyPDFDirectoryLoader(DOCS_FOLDER)
    raw_docs = loader.load()
    print(f"   Loaded {len(raw_docs)} pages from your documents.")

    # Split into smaller chunks (LLMs can't read 100-page PDFs at once)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(raw_docs)
    print(f"   Split into {len(chunks)} chunks.")

    # Create embeddings (converts text → numbers so we can search by meaning)
    print("Creating embeddings (this may take a minute)...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

    # Store everything in Chroma (a local vector database)
    print("Saving to Chroma vector database...")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_FOLDER
    )
    print(f"Done! Vector database saved to {CHROMA_FOLDER}")
    print(f"   You can now run the app.")

if __name__ == "__main__":
    ingest_documents()