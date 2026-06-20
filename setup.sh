#!/bin/bash

echo "🚀 RAG PDF Q&A - Quick Setup"
echo "=============================="
echo ""

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✓ Python found: $(python --version)"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo ""
    echo "📦 Creating virtual environment..."
    python -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install -r requirements.txt
echo "✓ Dependencies installed"

# Create .env file
if [ ! -f ".env" ]; then
    echo ""
    echo "⚙️  Creating .env file..."
    cp .env.example .env
    echo "✓ .env created"
    echo ""
    echo "⚠️  IMPORTANT: Edit .env and add your ANTHROPIC_API_KEY"
    echo "   Get your API key from: https://console.anthropic.com"
    echo ""
fi

# Create data directories
mkdir -p data/uploads
mkdir -p data/embeddings

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your ANTHROPIC_API_KEY"
echo "2. Run: python app.py"
echo "3. Open: http://localhost:5000"
echo ""
