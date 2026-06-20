import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
    UPLOAD_FOLDER = 'data/uploads'
    EMBEDDINGS_FOLDER = 'data/embeddings'
    MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB
    ALLOWED_EXTENSIONS = {'pdf'}
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
os.makedirs(Config.EMBEDDINGS_FOLDER, exist_ok=True)
