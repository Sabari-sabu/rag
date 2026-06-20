@echo off
echo.
echo 🚀 RAG PDF Q^&A - Quick Setup
echo ==============================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8+ first.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✓ Python found: %PYTHON_VERSION%

REM Create virtual environment
if not exist "venv" (
    echo.
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo ✓ Virtual environment created
) else (
    echo ✓ Virtual environment already exists
)

REM Activate virtual environment
echo.
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo 📥 Installing dependencies...
pip install -r requirements.txt
echo ✓ Dependencies installed

REM Create .env file
if not exist ".env" (
    echo.
    echo ⚙️  Creating .env file...
    copy .env.example .env
    echo ✓ .env created
    echo.
    echo ⚠️  IMPORTANT: Edit .env and add your ANTHROPIC_API_KEY
    echo    Get your API key from: https://console.anthropic.com
    echo.
)

REM Create data directories
if not exist "data\uploads" mkdir data\uploads
if not exist "data\embeddings" mkdir data\embeddings

echo.
echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Edit .env and add your ANTHROPIC_API_KEY
echo 2. Run: python app.py
echo 3. Open: http://localhost:5000
echo.
pause
