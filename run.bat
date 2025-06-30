@echo off
:: Simple batch script to run Python GUI application
:: Checks for Python and requirements before running

echo Checking for Python installation...

:: Check if Python is installed
echo INFO: make sure python is installed
echo Please install Python 3.x from https://www.python.org/downloads/
pause



:: Install requirements if file exists
if exist "requirements.txt" (
    echo Installing dependencies...
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    
    if %ERRORLEVEL% neq 0 (
        echo Error: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    echo No requirements.txt found - skipping dependency installation
)

:: Run the application
echo Starting application...
python gui.py

if %ERRORLEVEL% neq 0 (
    echo Error: Application failed to start (Error code: %ERRORLEVEL%)
    pause
    exit /b 1
)

echo Application closed successfully
pause
exit /b 0