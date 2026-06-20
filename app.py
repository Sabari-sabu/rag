from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import tempfile
from dotenv import load_dotenv

load_dotenv()

# Import utilities (pdf processor uses tempfiles, no disk persistence needed)
from utils_pdf_processor import extract_text_from_pdf, chunk_text
from utils_embeddings import find_relevant_chunks, answer_question

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

@app.route('/')
def index():
    """Serve the main HTML page."""
    return send_from_directory('.', 'index.html')

@app.route('/api/upload', methods=['POST'])
def upload_pdf():
    """Upload and process PDF — returns chunks as JSON (stateless)."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'error': 'Only PDF files allowed'}), 400

    try:
        # Use a temp file for processing — no persistent disk storage needed
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp:
            file.save(tmp.name)
            tmp_path = tmp.name

        text = extract_text_from_pdf(tmp_path)
        chunks = chunk_text(text)
        os.unlink(tmp_path)  # clean up temp file immediately

        return jsonify({
            'success': True,
            'message': f'PDF "{file.filename}" processed successfully',
            'chunks': chunks,
            'count': len(chunks),
            'filename': file.filename
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/ask', methods=['POST'])
def ask_question():
    """Answer question — receives chunks in request body (stateless)."""
    data = request.json or {}
    query = data.get('query', '')
    chunks = data.get('chunks', [])

    if not query:
        return jsonify({'error': 'No query provided'}), 400

    if not chunks:
        return jsonify({'error': 'No document chunks provided. Please upload a PDF first.'}), 400

    try:
        relevant_chunks = find_relevant_chunks(query, chunks, top_k=3)
        answer = answer_question(query, relevant_chunks)

        return jsonify({
            'success': True,
            'question': query,
            'answer': answer,
            'sources': relevant_chunks
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
