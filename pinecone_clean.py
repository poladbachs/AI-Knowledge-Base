import os
import pinecone
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

# ✅ Connect to Pinecone
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

# ✅ DELETE ALL EXISTING DATA
index.delete(delete_all=True)
print("🔥 Pinecone index cleared. Re-ingest new data now.")
