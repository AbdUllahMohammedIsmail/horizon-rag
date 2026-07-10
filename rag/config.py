import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

LLM_MODEL = "gemini-3.5-flash"

VECTOR_DB_PATH = "chroma_db"

PDF_PATH = "data/Horizon_Tours_Complete_Knowledge_Base_2025.pdf"