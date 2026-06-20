import PyPDF2
import json
import os
from config import Config

def extract_text_from_pdf(filepath):
    """Extract text from PDF file."""
    text = ""
    try:
        with open(filepath, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += f"\n--- Page {page_num + 1} ---\n"
                text += page.extract_text()
        return text
    except Exception as e:
        raise Exception(f"Error reading PDF: {str(e)}")

def chunk_text(text, chunk_size=Config.CHUNK_SIZE, overlap=Config.CHUNK_OVERLAP):
    """Split text into chunks with overlap."""
    # Clean text to remove invalid unicode characters
    text = text.encode('utf-8', errors='ignore').decode('utf-8')
    
    chunks = []
    words = text.split()

    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk)

    return chunks

def save_chunks(filename, chunks):
    """Save chunks to JSON file."""
    filepath = os.path.join(Config.EMBEDDINGS_FOLDER, f"{filename}.json")
    # Clean chunks to remove invalid unicode characters
    cleaned_chunks = []
    for chunk in chunks:
        # Remove invalid unicode surrogates
        cleaned_chunk = chunk.encode('utf-8', errors='ignore').decode('utf-8')
        cleaned_chunks.append(cleaned_chunk)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump({'chunks': cleaned_chunks, 'filename': filename}, f, ensure_ascii=False)
    return filepath

def load_chunks(filename):
    """Load chunks from JSON file."""
    filepath = os.path.join(Config.EMBEDDINGS_FOLDER, f"{filename}.json")
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['chunks']
    return []
