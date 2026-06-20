@echo off
echo.
echo Starting RAG PDF Q^&A Application...
echo.
echo Make sure Python and npm are installed!
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed
    pause
    exit /b 1
)

REM Check if npm is installed
npm --version >nul 2>&1
if errorlevel 1 (
    echo Error: npm is not installed
    pause
    exit /b 1
)

echo Starting Flask server on http://localhost:5000
echo.
python app.py
