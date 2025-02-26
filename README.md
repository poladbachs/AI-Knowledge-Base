# 🏆 Spitch AI Knowledge Base

## 🚀 Overview
**Spitch AI Knowledge Base** is an **AI-powered question-answering system** designed specifically for **Spitch AI**. It provides instant, accurate responses to questions about Spitch AI’s **technologies, security, compliance, and industry applications** using **advanced Natural Language Processing (NLP)** and **semantic search**.

This project is a **company-specific AI knowledge base**, making it **highly relevant for Spitch AI’s needs and its potential clients.**

---

## Demo
![Image](https://github.com/user-attachments/assets/95ba5274-d2ff-4412-a6c1-fe3e28c3d036)

---

## 🔥 Key Features

✅ **AI-Powered Search** – Retrieves the most relevant answers using **local embeddings (BAAI/bge-small-en) and Pinecone vector search**.

✅ **Company-Specific Knowledge** – Built exclusively for **Spitch AI**, ensuring precise and domain-specific responses.

✅ **Fast & Scalable** – Uses **FastAPI** for a high-performance backend and **Streamlit** for an intuitive UI.

✅ **Secure & Private** – No reliance on external APIs like OpenAI; everything runs **locally** with privacy-first embeddings.

✅ **Industry-Specific Insights** – Answers about **Spitch AI’s applications in Banking, Call Centers, Telecom, and Government.**

✅ **Real-Time Updates** – Easily update knowledge by modifying the data and re-ingesting into Pinecone.

✅ **Customizable UI** – Premium Streamlit interface with an elegant **Spitch AI-branded design**.

---

## 🛠️ Tech Stack

| Technology    | Purpose |
|--------------|----------|
| **Python** | Core programming language |
| **FastAPI** | High-performance backend API |
| **Streamlit** | Interactive UI for querying Spitch AI knowledge |
| **Pinecone** | Vector database for fast similarity search |
| **Sentence Transformers** | Local embedding model (**BAAI/bge-small-en**) for AI-driven search |
| **LangChain** | Manages text chunking and vector store operations |

---

## 📌 How It Works

1️⃣ **Data Ingestion** – Spitch AI’s knowledge is converted into vector embeddings and stored in **Pinecone**.

2️⃣ **AI Search** – A user’s query is transformed into a vector and compared against stored knowledge.

3️⃣ **Semantic Matching** – The best-matching answer is retrieved based on **meaning, not just keywords**.

4️⃣ **Real-Time Answers** – The system returns the most relevant response instantly.

---

## 🎯 Why This Project is a Perfect Fit for Spitch AI

✅ **Tailored to Spitch AI** – Unlike generic AI knowledge bases, this is built **specifically** for Spitch AI.

✅ **Company Branding & Customization** – The knowledge aligns with **Spitch AI’s identity & services**.

✅ **Future-Proof & Scalable** – Knowledge can be expanded easily **without changing the architecture**.

✅ **Replaces Traditional FAQs** – Eliminates static FAQs with a **dynamic, AI-powered knowledge system**.

✅ **Attracts Potential Clients** – Enhances Spitch AI’s ability to showcase its **AI capabilities to new customers**.

---

## 🔧 Setup & Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/spitch-ai-knowledge-base.git
cd spitch-ai-knowledge-base

# Install dependencies
pip install -r requirements.txt

# Set environment variables (.env)
PINECONE_API_KEY="your_pinecone_api_key"
PINECONE_ENV="your_pinecone_region"
PINECONE_INDEX="spitch-knowledge-base"

# Run API
uvicorn query_knowledge:app --reload

# Run Streamlit UI
streamlit run streamlit_app.py
```

---

## 🚀 Usage

### 1️⃣ **Ingest Data into Pinecone**
```bash
python3 pinecone_clean.py  # Clears previous data
python3 ingest_data.py  # Uploads updated knowledge
```

### 2️⃣ **Start FastAPI Backend**
```bash
uvicorn query_knowledge:app --reload
```

### 3️⃣ **Run the Streamlit UI**
```bash
streamlit run streamlit_app.py
```
