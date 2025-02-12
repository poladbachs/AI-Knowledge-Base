import os
import time
import pinecone
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from vector_db import vector_store, embedding_model

spitch_knowledge = [
    # ✅ Core Company Information
    "Spitch AI is a leading provider of AI-driven speech recognition, voice biometrics, and natural language processing (NLP) solutions.",
    "Spitch AI specializes in automating and optimizing voice-based interactions for businesses across various industries.",
    "Spitch AI enables enterprises to improve customer experience through real-time speech analytics and AI-powered automation.",

    # ✅ Technologies & AI Capabilities
    "Spitch AI uses advanced natural language processing (NLP) and deep learning to accurately process and understand speech.",
    "Spitch AI's voice biometrics technology ensures secure authentication by analyzing unique vocal characteristics.",
    "Spitch AI leverages machine learning algorithms to enhance speech-to-text accuracy and sentiment analysis.",
    "Spitch AI provides automatic speech recognition (ASR) technology for multilingual voice-based applications.",

    # ✅ Security & Compliance
    "Spitch AI ensures full compliance with GDPR and ISO 27001 for secure voice data processing and user authentication.",
    "Spitch AI's biometric authentication prevents fraud by verifying users through their unique voice patterns.",
    "Spitch AI's speech encryption and secure voice authentication help businesses meet regulatory compliance standards.",

    # ✅ Industry Use Cases
    "Banks use Spitch AI to enable voice authentication for secure transactions and fraud prevention.",
    "Call centers leverage Spitch AI for AI-driven customer support automation and real-time speech analytics.",
    "Government agencies use Spitch AI for voice-based identity verification and secure citizen services.",
    "Telecom companies implement Spitch AI to improve call routing and automate customer self-service.",
    "Healthcare providers use Spitch AI for voice-enabled patient authentication and medical data security.",
    "Insurance firms integrate Spitch AI for automated claims processing and fraud detection.",
    
    # ✅ Competitive Edge & Unique Features
    "Spitch AI offers fully customizable AI models, allowing businesses to tailor voice recognition to their specific needs.",
    "Unlike generic AI solutions, Spitch AI provides deep industry expertise and custom NLP models for voice applications.",
    "Spitch AI enables omnichannel integration, allowing businesses to deploy AI-powered voice technology across multiple platforms."
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