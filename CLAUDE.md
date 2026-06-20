# RAG PDF Q&A Project

## Quick Start

1. **Setup environment**:
   - Windows: `setup.bat`
   - macOS/Linux: `bash setup.sh`

2. **Configure API key**:
   - Edit `.env` and add `ANTHROPIC_API_KEY=your_key_here`
   - Get key from: https://console.anthropic.com

3. **Run application**:

   ```bash
   # Activate virtual environment (if needed)
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate  # Windows

   # Start backend
   python app.py
   ```

4. **Access frontend**:
   - Open browser: http://localhost:5000

## Architecture

### Backend (Flask)

- **app.py**: Main API server with three endpoints
  - POST `/api/upload`: Process and store PDF chunks
  - POST `/api/ask`: Generate answers from relevant chunks
  - GET `/api/files`: List uploaded documents

- **utils_pdf_processor.py**: PDF extraction and chunking
  - Uses PyPDF2 for text extraction
  - Splits into overlapping chunks for context

- **utils_embeddings.py**: RAG logic using Claude API
  - Keyword-based chunk retrieval (can be upgraded to vector embeddings)
  - Claude 3.5 Sonnet for answer generation

- **config.py**: Configuration and data directories

### Frontend (HTML/CSS/JS)

- **index.html**: Single-page application
  - Drag-and-drop file upload
  - Document selection and management
  - Question input and answer display

## Data Flow

```
PDF Upload → Extract Text → Split into Chunks → Store JSON
                                                      ↓
Query + Document → Retrieve Relevant Chunks → Claude API → Answer
```

## Configuration

Edit `config.py` to adjust:

- `CHUNK_SIZE`: Words per chunk (default 500)
- `CHUNK_OVERLAP`: Overlap between chunks (default 50)
- `MAX_FILE_SIZE`: Max upload size (default 50MB)
- `UPLOAD_FOLDER`: PDF storage location
- `EMBEDDINGS_FOLDER`: Chunk storage location

## Storage Structure

```
data/
├── uploads/
│   ├── document1.pdf
│   └── document2.pdf
└── embeddings/
    ├── document1.pdf.json
    └── document2.pdf.json
```

Each JSON file contains:

```json
{
  "filename": "document.pdf",
  "chunks": ["chunk1 text...", "chunk2 text...", ...]
}
```

## API Keys

The application requires:

- **Anthropic API Key**: For Claude models
  - Get from: https://console.anthropic.com
  - Set in: `.env` file as `ANTHROPIC_API_KEY`

## Limitations & Future Work

### Current Limitations

- Simple keyword-based retrieval (not vector embeddings)
- Single document context per query
- No chat history or session persistence
- Basic chunk overlapping strategy

### Potential Improvements

- Implement real vector embeddings (OpenAI, Anthropic)
- Add vector database (Pinecone, Weaviate, Chroma)
- Multi-document queries
- User authentication
- Chat history and export
- Custom system prompts
- Streaming responses
- Better chunk retrieval strategies
- Document metadata (author, date, etc.)

## Dependencies

See `requirements.txt`:

- Flask: Web framework
- Flask-CORS: Cross-origin support
- anthropic: Claude API client
- PyPDF2: PDF processing
- python-dotenv: Environment variables

## Testing

Manual testing workflow:

1. Upload a sample PDF
2. Try various questions about the content
3. Check answer quality and relevance
4. Test edge cases (empty queries, missing documents)

## Troubleshooting

### API Key Issues

- Ensure `.env` file exists in root directory
- Check key is copied exactly from Anthropic console
- No extra spaces or quotes

### Port Already in Use

- Flask default is port 5000
- Change in `app.py`: `app.run(port=5001)`

### CORS Errors

- Frontend should access via `http://localhost:5000`
- CORS already enabled in Flask app

### PDF Upload Failures

- Check file is valid PDF
- File size under 50MB
- Check `data/uploads/` directory permissions
