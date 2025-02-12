import os
import pinecone
from sentence_transformers import SentenceTransformer
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

embedding_model = SentenceTransformer("BAAI/bge-small-en")

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

def query_knowledge_base(question: str, top_k=3):
    if " it " in question.lower():
        question = "Spitch AI " + question.lstrip("it ")

    query_embedding = embedding_model.encode(question).tolist()
    result = index.query(vector=query_embedding, top_k=top_k, include_metadata=True)

    if "matches" in result and result["matches"]:
        best_match = result["matches"][0]
        similarity_score = best_match["score"]
        best_answer = best_match["metadata"].get("text", "")

        print(f"🔍 Query: {question} | Best Match Score: {similarity_score} | Answer: {best_answer}")

        query_words = set(question.lower().split())
        answer_words = set(best_answer.lower().split())

        common_words = query_words & answer_words

        if similarity_score < 0.5 or (len(common_words) < 2 and "spitch ai" not in question.lower()):
            return {"answer": "🤔 No relevant answer found. Try rephrasing your question!"}

        return {"answer": best_answer}

    return {"answer": "🤔 No relevant answer found. Try rephrasing your question!"}


@app.post("/query")
def get_answer(request: QueryRequest):
    response = query_knowledge_base(request.query)
    return response