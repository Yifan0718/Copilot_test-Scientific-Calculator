#!/bin/bash
# Scientific Calculator Launcher Script
# Automatically detects the best version to run

echo "🧮 Scientific Calculator - FX991 Style"
echo "======================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3 and try again."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Try to run GUI version first
echo "🔍 Checking for GUI support (tkinter)..."

if python3 -c "import tkinter" 2>/dev/null; then
    echo "✅ GUI support available - Starting GUI calculator..."
    python3 calculator.py
else
    echo "⚠️  GUI support not available - Starting command-line calculator..."
    echo "   (To use GUI: install tkinter with your package manager)"
    python3 calculator_cli.py
fi