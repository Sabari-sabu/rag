#!/bin/bash

echo ""
echo "Starting RAG PDF Q&A Application..."
echo ""

# Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Error: Python is not installed"
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "Error: npm is not installed"
    exit 1
fi

echo "Starting Flask server on http://localhost:5000"
echo ""
python app.py
