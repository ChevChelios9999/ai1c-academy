@echo off
setlocal

cd /d "%~dp0"

if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

call ".venv\Scripts\activate.bat"

echo Installing dependencies...
REM Use "python -m pip" (not "pip") - on Windows pip.exe cannot overwrite itself
REM while it is the running process.
python -m pip install --quiet --upgrade pip
python -m pip install --quiet -r requirements.txt

if not exist ".env" (
    copy /y ".env.example" ".env" >nul
    echo Created .env from .env.example - edit it if needed.
)

echo Starting app at http://127.0.0.1:8501 ...
streamlit run app\Home.py

endlocal
