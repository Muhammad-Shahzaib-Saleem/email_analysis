import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama3-8b-8192"
QWEN_MODEL = "qwen/qwq-32b:free"
DEEP_SEEK_MODEL="deepseek/deepseek-chat-v3-0324:free"
LLAMA_MODEL="meta-llama/llama-4-maverick:free"

OPEN_ROUTER_API="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"
OPEN_ROUTER_API_1="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"

# Vector Database Configuration
VECTOR_DB_PATH = "./vector_db"
COLLECTION_NAME = "email_collection"

# Embedding Model Configuration
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# File Upload Configuration
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB
SUPPORTED_FORMATS = ['.csv', '.json', '.txt','.eml']

# Streamlit Configuration
PAGE_TITLE = "Email Analysis System"
PAGE_ICON = "📧"