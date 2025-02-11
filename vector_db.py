import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import Pinecone as PineconeVectorStore
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

pc = Pinecone(api_key=PINECONE_API_KEY)

if PINECONE_INDEX not in pc.list_indexes().names():
    pc.create_index(
        name=PINECONE_INDEX,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region=PINECONE_ENV)
    )

embedding_model = SentenceTransformer("BAAI/bge-small-en")

vector_store = pc.Index(PINECONE_INDEX)