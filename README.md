# 🧮 科学计算器

一个功能完整的科学计算器应用程序，模仿卡西欧FX991等流行计算器的功能。提供图形用户界面(GUI)和命令行界面(CLI)两种版本，支持Windows和Linux平台。

## ✨ Features

### 📱 Basic Calculator Functions
- **Arithmetic Operations**: Addition (+), Subtraction (-), Multiplication (×), Division (÷)
- **Advanced Operations**: Power (xʸ), Modulo (%), Parentheses support
- **Memory Functions**: Memory Clear (MC), Memory Recall (MR), Memory Add (M+), Memory Subtract (M-)

### 🔬 Scientific Functions
- **Trigonometric Functions**: sin, cos, tan (with degree/radian mode switching)
- **Logarithmic Functions**: log₁₀(x), ln(x)
- **Power Functions**: x², √x, xʸ, 1/x
- **Special Functions**: n! (factorial)
- **Mathematical Constants**: π (pi), e (Euler's number)

### 🎯 Advanced Features
- **Dual Angle Modes**: Switch between degrees and radians
- **Error Handling**: Comprehensive error checking for invalid operations
- **Keyboard Support**: Full keyboard shortcuts in GUI mode
- **Cross-Platform**: Works on Windows and Linux
- **Two Interfaces**: GUI (tkinter) and CLI versions available

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- For GUI version: tkinter (usually included with Python)

### Installation and Running

#### Option 1: GUI Version (Recommended)
```bash
# Clone or download the repository
git clone https://github.com/Yifan0718/Copilot_test.git
cd Copilot_test

# Run the GUI calculator
python3 calculator.py
```

#### Option 2: Command Line Version
```bash
# Run the CLI calculator (works in any environment)
python3 calculator_cli.py
```

#### Option 3: Test Core Functionality
```bash
# Run tests and see a demo of all features
python3 test_calculator.py
```

## 💻 Platform-Specific Instructions

### 🐧 Linux (Ubuntu/Debian)

```bash
# Install Python and tkinter (if not already installed)
sudo apt update
sudo apt install python3 python3-tk

# Run the calculator
python3 calculator.py
```

### 🐧 Linux (CentOS/RHEL/Fedora)

```bash
# Install Python and tkinter
sudo yum install python3 python3-tkinter  # CentOS/RHEL
# OR
sudo dnf install python3 python3-tkinter  # Fedora

# Run the calculator
python3 calculator.py
```

### 🪟 Windows

#### Method 1: Using Python from python.org
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Install Python (make sure to check "Add Python to PATH")
3. Open Command Prompt or PowerShell
4. Navigate to the calculator directory
5. Run: `python calculator.py`

#### Method 2: Using Microsoft Store Python
1. Install Python from Microsoft Store
2. Open Command Prompt or PowerShell
3. Navigate to the calculator directory
4. Run: `python calculator.py`

#### Method 3: Creating a Batch File (Windows)
Create a file named `run_calculator.bat`:
```batch
@echo off
python calculator.py
pause
```
Double-click the batch file to run the calculator.

## 📖 Usage Guide

### GUI Version

#### Basic Operations
- Click number buttons (0-9) to enter numbers
- Use operation buttons (+, -, ×, ÷) for arithmetic
- Press = or Enter to calculate results
- Use C to clear all, ⌫ for backspace

#### Scientific Functions
- **Trigonometric**: sin, cos, tan buttons
- **Powers**: x², √, xʸ buttons  
- **Logarithms**: log (base 10), ln (natural log)
- **Special**: n! for factorial, 1/x for reciprocal

#### Memory Operations
- **MC**: Clear memory
- **MR**: Recall memory value
- **M+**: Add current display to memory
- **M-**: Subtract current display from memory

#### Angle Mode
- Click "DEG/RAD" to switch between degree and radian modes
- Current mode is displayed in the top-left corner

#### Keyboard Shortcuts
- Numbers 0-9: Enter numbers
- +, -, *, /: Basic operations
- Enter or =: Calculate
- Escape: Clear all
- Backspace: Delete last character

### Command Line Version

#### Basic Usage
```bash
python3 calculator_cli.py
```

#### Example Calculations
```
[DEG] calc> 2+3*4
= 14

[DEG] calc> sin(30)
= 0.5

[DEG] calc> sqrt(16)
= 4

[DEG] calc> log(100)
= 2

[DEG] calc> fact(5)
= 120

[DEG] calc> pi*2
= 6.283185307
```

#### Commands
- `deg` / `rad`: Switch angle mode
- `mc`: Clear memory
- `mr`: Recall memory
- `m+`: Add to memory
- `m-`: Subtract from memory
- `help`: Show help
- `quit` / `exit`: Exit calculator

## 🧪 Testing

Run the comprehensive test suite:
```bash
python3 test_calculator.py
```

This will test:
- Basic arithmetic operations
- Scientific functions
- Error handling
- Result formatting
- Interactive demo of all features

## 📁 Project Structure

```
Copilot_test/
├── calculator.py          # Main GUI calculator application
├── calculator_cli.py      # Command-line calculator
├── test_calculator.py     # Test suite and functionality demo
├── requirements.txt       # Python dependencies (minimal)
├── README.md             # This documentation
└── .gitignore           # Git ignore file
```

## 🔧 Troubleshooting

### GUI Not Working?
1. **Linux**: Install tkinter
   ```bash
   sudo apt install python3-tk  # Ubuntu/Debian
   sudo yum install python3-tkinter  # CentOS/RHEL
   ```

2. **Windows**: Reinstall Python with "tcl/tk and IDLE" option checked

3. **Alternative**: Use the command-line version
   ```bash
   python3 calculator_cli.py
   ```

### Permission Issues?
```bash
chmod +x calculator.py
chmod +x calculator_cli.py
```

### Python Not Found?
- **Windows**: Add Python to PATH or use full path
- **Linux**: Install Python 3
  ```bash
  sudo apt install python3  # Ubuntu/Debian
  ```

## 🎯 Advanced Usage

### Batch Calculations
Create a Python script for multiple calculations:
```python
from calculator_cli import CommandLineCalculator

calc = CommandLineCalculator()
expressions = ["2+2", "sin(45)", "sqrt(16)", "log(100)"]

for expr in expressions:
    result = calc.evaluate(expr)
    print(f"{expr} = {result}")
```

### Integration with Other Scripts
```python
# Import the calculator core
from test_calculator import CalculatorCore

calc = CalculatorCore()
result = calc.binary_operation(5, 3, '+')  # Returns 8
scientific_result = calc.function_operation(30, 'sin')  # Returns 0.5
```

## 🐛 Known Limitations

1. **Complex Numbers**: Limited support for complex number operations
2. **Large Numbers**: Scientific notation used for very large/small numbers
3. **Precision**: Standard Python float precision limitations
4. **GUI Dependencies**: GUI version requires tkinter installation

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📞 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Run the test suite to verify functionality
3. Try the command-line version as an alternative
4. Open an issue on GitHub with details about your environment

---

**Made with ❤️ - A comprehensive scientific calculator for everyone!**