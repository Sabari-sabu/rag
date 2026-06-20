# RAG PDF Q&A Application

A simple Retrieval-Augmented Generation (RAG) application that lets you upload PDF documents and ask questions about their content. The application uses Claude AI for intelligent question answering.

## Features

- 📤 Drag-and-drop PDF upload
- 🔍 Intelligent context retrieval from documents
- 💬 Question answering powered by Claude AI
- 📱 Clean, modern web interface
- 🎯 Real-time file management

## Project Structure

```
rag/
├── app.py                    # Flask backend API
├── config.py                 # Configuration settings
├── utils_pdf_processor.py    # PDF processing utilities
├── utils_embeddings.py       # Embedding and QA utilities
├── index.html                # Frontend web interface
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── data/
│   ├── uploads/             # Uploaded PDF files
│   └── embeddings/          # Processed chunks storage
└── README.md
```

## Setup Instructions

### 1. Get Your Anthropic API Key

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up or log in
3. Create an API key in the account settings
4. Copy your API key

### 2. Install Dependencies

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API key
# ANTHROPIC_API_KEY=your_actual_api_key_here
```

Or on Windows:

```bash
copy .env.example .env
# Then edit .env with your API key
```

### 4. Run the Application

**Using npm (recommended)**:
```bash
npm run dev
```

**Or directly with Python**:
```bash
python app.py
```

The application will be available at: `http://localhost:5000`

### 5. Access the Frontend

Open your browser and go to:

```
http://localhost:5000
```

Or open the `index.html` file directly (note: direct file access won't work - you need the Flask server running).

## Usage

### Available npm Commands

```bash
# Start development server
npm run dev

# Start server (same as dev)
npm start

# Install Python dependencies
npm run setup

# Run health check
npm test
```

## API Endpoints

### Upload PDF

```
POST /api/upload
Content-Type: multipart/form-data

Response:
{
  "success": true,
  "message": "PDF uploaded and processed",
  "chunks": 42,
  "filename": "document.pdf"
}
```

### Ask Question

```
POST /api/ask
Content-Type: application/json

Request Body:
{
  "query": "What is the main topic?",
  "filename": "document.pdf"
}

Response:
{
  "success": true,
  "question": "What is the main topic?",
  "answer": "Based on the document...",
  "sources": ["excerpt 1", "excerpt 2", "excerpt 3"]
}
```

### List Files

```
GET /api/files

Response:
{
  "files": [
    {"name": "document.pdf", "size": 102400},
    ...
  ]
}
```

### Health Check

```
GET /api/health

Response:
{
  "status": "ok"
}
```

## Configuration

Edit `config.py` to customize:

- `CHUNK_SIZE`: Number of words per text chunk (default: 500)
- `CHUNK_OVERLAP`: Overlap between chunks (default: 50)
- `MAX_FILE_SIZE`: Maximum upload size (default: 50MB)
- `UPLOAD_FOLDER`: Where to store PDFs
- `EMBEDDINGS_FOLDER`: Where to store processed chunks

## How It Works

1. **PDF Processing**: PDFs are extracted into text and split into overlapping chunks
2. **Query Processing**: When you ask a question, the system finds the most relevant chunks using keyword similarity
3. **Answer Generation**: Claude AI generates an answer based on the relevant context
4. **Source Display**: The most relevant text excerpts are shown as sources

## Troubleshooting

### "Cannot find module" errors

```bash
# Make sure your virtual environment is activated and dependencies are installed
pip install -r requirements.txt
```

### "API key not found" error

- Check that `.env` file exists in the project root
- Verify `ANTHROPIC_API_KEY` is set correctly in `.env`
- Make sure there are no extra spaces in the API key

### CORS errors

- The Flask backend has CORS enabled
- If issues persist, check that the frontend is accessing `http://localhost:5000`

### PDF upload fails

- Check file is valid PDF format
- File size should be under 50MB
- Check file permissions

## Future Improvements

- Better embedding using Anthropic or OpenAI APIs
- Vector database (Pinecone, Weaviate) for larger document sets
- Multiple PDF comparison
- Chat history
- Custom prompt engineering
- Export answers as PDF
- User authentication

## License

This project is provided as-is for educational purposes.
