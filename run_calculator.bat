@echo off
REM Scientific Calculator Launcher Script for Windows
REM Automatically detects the best version to run

echo 🧮 Scientific Calculator - FX991 Style
echo =======================================

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python from python.org and try again.
    pause
    exit /b 1
)

echo ✅ Python found
python --version

REM Try to run GUI version first
echo 🔍 Checking for GUI support (tkinter)...

python -c "import tkinter" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ GUI support available - Starting GUI calculator...
    python calculator.py
) else (
    echo ⚠️  GUI support not available - Starting command-line calculator...
    echo    ^(To use GUI: reinstall Python with tkinter support^)
    python calculator_cli.py
)

pause