import os
import time
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from vector_db import vector_store, embedding_model

spitch_knowledge([
    # General Knowledge
    "Spitch.ai provides AI-powered speech analytics to improve customer interactions.",
    "Spitch's Voice Biometrics allows for secure and fraud-resistant user authentication.",
    "The AI Knowledge Base by Spitch helps customer agents find accurate responses quickly.",
    "Spitch integrates Conversational AI and NLP to improve virtual assistants and chatbots.",
    "Voice authentication by Spitch replaces passwords with secure voice-based login.",
    "Spitch's solutions are used in call centers to automate support and analyze customer sentiment.",

    # ✅ New Knowledge - Technologies & AI Capabilities
    "Spitch uses advanced NLP, speech recognition, and AI-driven automation.",
    "Spitch's core technologies include conversational AI, speech analytics, and voice biometrics.",
    "Spitch AI solutions leverage machine learning models for improved speech understanding.",
    "Spitch's AI platform is designed to automate customer interactions using voice and text.",
    "Spitch integrates with cloud and on-premise systems for seamless AI deployment.",

    # ✅ New Knowledge - Use Cases & Industries
    "Spitch AI is used in banking to improve customer authentication and fraud prevention.",
    "Insurance companies use Spitch for automated customer service and claim processing.",
    "Spitch provides AI-powered solutions for telecom companies to manage high-volume customer inquiries.",
    "Spitch helps government agencies with voice recognition-based identity verification.",
    "Retail companies use Spitch AI to enhance customer experience in e-commerce and support centers.",

    # ✅ New Knowledge - Competitive Edge & Features
    "Spitch differentiates itself by offering fully customizable AI models for enterprises.",
    "Spitch's speech analytics system provides deep insights into customer interactions.",
    "Spitch AI's voice authentication technology eliminates the need for passwords.",
    "Spitch offers multi-language support, allowing businesses to deploy AI globally.",
    "Spitch AI enables seamless omnichannel support through voice, chat, and email integration."
])


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