@echo off
REM Activate your virtual environment
call venv\Scripts\activate.bat

REM Run uvicorn; port will be read inside app from .env automatically
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
