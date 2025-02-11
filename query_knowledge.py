import os
from fastapi import FastAPI
from pydantic import BaseModel
from vector_db import vector_store, embedding_model

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_knowledge(request: QueryRequest):
    query_text = request.query
    query_embedding = embedding_model.encode(query_text).tolist()
    
    search_results = vector_store.query(vector=query_embedding, top_k=5, include_metadata=True)

    matches = search_results.get("matches", [])
    if not matches:
        return {"answer": "No relevant knowledge found."}

    best_match = max(matches, key=lambda x: x.get("score", 0))
    
    actual_sentence = best_match.get("metadata", {}).get("text", "No text available")

    return {"answer": actual_sentence}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
