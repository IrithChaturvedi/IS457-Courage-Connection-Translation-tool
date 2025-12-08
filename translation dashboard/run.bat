@echo off
echo Starting Courage Connection Translation Dashboard...

REM Navigate to the project directory (auto-detects the folder of the .bat file)
cd /d "%~dp0"

REM Activate virtual environment
call venv\Scripts\activate

REM Run the Flask application
start "" http://127.0.0.1:5000
python app.py

REM Keep window open after exit
pause
