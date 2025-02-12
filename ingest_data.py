import os
import time
import pinecone
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from vector_db import vector_store, embedding_model

spitch_knowledge = [
    "Spitch AI is a company that develops AI-powered speech recognition and voice authentication technology.",
    "Spitch AI specializes in voice biometrics, speech analytics, and AI-driven customer interactions.",
    "Spitch AI provides solutions that replace passwords with secure voice authentication.",
    "Spitch AI supports multiple languages and integrates with existing business platforms.",
    "Spitch AI ensures GDPR and ISO 27001 compliance in voice data processing.",
    "Spitch AI's biometric authentication prevents fraud and unauthorized access.",

    "Spitch AI enables voice authentication for secure transactions and fraud detection.",
    "Spitch AI automates customer support with AI-driven speech recognition.",
    "Spitch AI provides voice-based identity verification for secure public services.",
    "Spitch AI improves call routing and customer self-service through AI-powered automation.",
]

def generate_knowledge_base():
    documents = [Document(page_content=text) for text in spitch_knowledge]

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    all_chunks = text_splitter.split_documents(documents)

    chunk_texts = [chunk.page_content for chunk in all_chunks]

    print(f"Uploading {len(chunk_texts)} text chunks to Pinecone...")

    for i, chunk in enumerate(chunk_texts):
        embedding = embedding_model.encode(chunk).tolist()
        vector_store.upsert(vectors=[(f"chunk_{i}", embedding, {"source": f"chunk_{i}", "text": chunk})])

        print(f"✅ Successfully uploaded chunk {i+1}/{len(chunk_texts)}")
        time.sleep(1)

    print("✅ Knowledge Base successfully stored in Pinecone!")

if __name__ == "__main__":
    generate_knowledge_base()