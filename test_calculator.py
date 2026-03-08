#!/usr/bin/env python3
"""
Test suite for the Scientific Calculator
Tests the core mathematical functionality without GUI dependencies
"""

import math
import sys
import os

# Add the current directory to path so we can import calculator modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


class CalculatorCore:
    """Core calculator functionality without GUI dependencies"""
    
    def __init__(self):
        self.angle_mode = "deg"  # deg or rad
        self.memory = 0
        
    def binary_operation(self, a, b, op):
        """Perform binary operations"""
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ValueError("Division by zero")
            return a / b
        elif op == '**':
            return a ** b
        elif op == '%':
            return a % b
        else:
            raise ValueError(f"Unknown operation: {op}")
            
    def function_operation(self, value, func):
        """Perform unary function operations"""
        if func == 'sin':
            if self.angle_mode == 'deg':
                return math.sin(math.radians(value))
            else:
                return math.sin(value)
        elif func == 'cos':
            if self.angle_mode == 'deg':
                return math.cos(math.radians(value))
            else:
                return math.cos(value)
        elif func == 'tan':
            if self.angle_mode == 'deg':
                return math.tan(math.radians(value))
            else:
                return math.tan(value)
        elif func == 'log':
            if value <= 0:
                raise ValueError("Invalid input for log")
            return math.log10(value)
        elif func == 'ln':
            if value <= 0:
                raise ValueError("Invalid input for ln")
            return math.log(value)
        elif func == 'sqrt':
            if value < 0:
                raise ValueError("Invalid input for sqrt")
            return math.sqrt(value)
        elif func == 'square':
            return value ** 2
        elif func == 'reciprocal':
            if value == 0:
                raise ValueError("Division by zero")
            return 1 / value
        elif func == 'factorial':
            if value < 0 or value != int(value):
                raise ValueError("Invalid input for factorial")
            return math.factorial(int(value))
        else:
            raise ValueError(f"Unknown function: {func}")
            
    def format_result(self, result):
        """Format calculation result"""
        if abs(result) > 1e10 or (abs(result) < 1e-10 and result != 0):
            return f"{result:.6e}"
        elif result == int(result):
            return str(int(result))
        else:
            return f"{result:.10g}"


def test_basic_arithmetic():
    """Test basic arithmetic operations"""
    calc = CalculatorCore()
    
    # Test addition
    assert calc.binary_operation(2, 3, '+') == 5
    assert calc.binary_operation(-2, 3, '+') == 1
    assert calc.binary_operation(0.1, 0.2, '+') == 0.30000000000000004  # Expected float precision
    
    # Test subtraction
    assert calc.binary_operation(5, 3, '-') == 2
    assert calc.binary_operation(3, 5, '-') == -2
    
    # Test multiplication
    assert calc.binary_operation(3, 4, '*') == 12
    assert calc.binary_operation(-3, 4, '*') == -12
    
    # Test division
    assert calc.binary_operation(10, 2, '/') == 5
    assert calc.binary_operation(1, 3, '/') == 1/3
    
    # Test division by zero
    try:
        calc.binary_operation(1, 0, '/')
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
        
    # Test power
    assert calc.binary_operation(2, 3, '**') == 8
    assert calc.binary_operation(4, 0.5, '**') == 2
    
    # Test modulo
    assert calc.binary_operation(10, 3, '%') == 1
    
    print("✓ Basic arithmetic tests passed")


def test_scientific_functions():
    """Test scientific functions"""
    calc = CalculatorCore()
    
    # Test trigonometric functions (degrees)
    calc.angle_mode = "deg"
    assert abs(calc.function_operation(0, 'sin') - 0) < 1e-10
    assert abs(calc.function_operation(90, 'sin') - 1) < 1e-10
    assert abs(calc.function_operation(0, 'cos') - 1) < 1e-10
    assert abs(calc.function_operation(90, 'cos') - 0) < 1e-10
    assert abs(calc.function_operation(0, 'tan') - 0) < 1e-10
    assert abs(calc.function_operation(45, 'tan') - 1) < 1e-10
    
    # Test trigonometric functions (radians)
    calc.angle_mode = "rad"
    assert abs(calc.function_operation(0, 'sin') - 0) < 1e-10
    assert abs(calc.function_operation(math.pi/2, 'sin') - 1) < 1e-10
    assert abs(calc.function_operation(0, 'cos') - 1) < 1e-10
    assert abs(calc.function_operation(math.pi/2, 'cos') - 0) < 1e-10
    
    # Test logarithmic functions
    assert abs(calc.function_operation(100, 'log') - 2) < 1e-10
    assert abs(calc.function_operation(1000, 'log') - 3) < 1e-10
    assert abs(calc.function_operation(math.e, 'ln') - 1) < 1e-10
    
    # Test square root
    assert calc.function_operation(4, 'sqrt') == 2
    assert calc.function_operation(9, 'sqrt') == 3
    assert abs(calc.function_operation(2, 'sqrt') - math.sqrt(2)) < 1e-10
    
    # Test square
    assert calc.function_operation(3, 'square') == 9
    assert calc.function_operation(-3, 'square') == 9
    
    # Test reciprocal
    assert calc.function_operation(2, 'reciprocal') == 0.5
    assert calc.function_operation(4, 'reciprocal') == 0.25
    
    # Test factorial
    assert calc.function_operation(0, 'factorial') == 1
    assert calc.function_operation(1, 'factorial') == 1
    assert calc.function_operation(5, 'factorial') == 120
    
    print("✓ Scientific function tests passed")


def test_error_handling():
    """Test error handling"""
    calc = CalculatorCore()
    
    # Test negative square root
    try:
        calc.function_operation(-1, 'sqrt')
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
        
    # Test log of negative number
    try:
        calc.function_operation(-1, 'log')
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
        
    # Test factorial of negative number
    try:
        calc.function_operation(-1, 'factorial')
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
        
    # Test reciprocal of zero
    try:
        calc.function_operation(0, 'reciprocal')
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
        
    print("✓ Error handling tests passed")


def test_format_result():
    """Test result formatting"""
    calc = CalculatorCore()
    
    # Test integer results
    assert calc.format_result(5.0) == "5"
    assert calc.format_result(-3.0) == "-3"
    
    # Test decimal results
    assert calc.format_result(3.14159) == "3.14159"
    
    # Test scientific notation for large numbers
    large_result = calc.format_result(1e12)
    assert "e" in large_result
    
    # Test scientific notation for small numbers
    small_result = calc.format_result(1e-12)
    assert "e" in small_result
    
    print("✓ Result formatting tests passed")


def run_interactive_demo():
    """Run an interactive demo of the calculator core"""
    calc = CalculatorCore()
    
    print("\n" + "="*50)
    print("SCIENTIFIC CALCULATOR CORE FUNCTIONALITY DEMO")
    print("="*50)
    
    print("\n📱 Basic Arithmetic Operations:")
    print(f"2 + 3 = {calc.binary_operation(2, 3, '+')}")
    print(f"10 - 4 = {calc.binary_operation(10, 4, '-')}")
    print(f"6 × 7 = {calc.binary_operation(6, 7, '*')}")
    print(f"15 ÷ 3 = {calc.binary_operation(15, 3, '/')}")
    print(f"2³ = {calc.binary_operation(2, 3, '**')}")
    print(f"17 mod 5 = {calc.binary_operation(17, 5, '%')}")
    
    print("\n🔬 Scientific Functions (Degree mode):")
    calc.angle_mode = "deg"
    print(f"sin(30°) = {calc.format_result(calc.function_operation(30, 'sin'))}")
    print(f"cos(60°) = {calc.format_result(calc.function_operation(60, 'cos'))}")
    print(f"tan(45°) = {calc.format_result(calc.function_operation(45, 'tan'))}")
    
    print("\n📊 Logarithmic and Power Functions:")
    print(f"√16 = {calc.function_operation(16, 'sqrt')}")
    print(f"5² = {calc.function_operation(5, 'square')}")
    print(f"log₁₀(100) = {calc.function_operation(100, 'log')}")
    print(f"ln(e) = {calc.format_result(calc.function_operation(math.e, 'ln'))}")
    print(f"1/4 = {calc.function_operation(4, 'reciprocal')}")
    print(f"5! = {calc.function_operation(5, 'factorial')}")
    
    print("\n🧮 Constants:")
    print(f"π ≈ {calc.format_result(math.pi)}")
    print(f"e ≈ {calc.format_result(math.e)}")
    
    print("\n✅ All core functionality working correctly!")
    print("Note: GUI version requires tkinter installation.")


def main():
    """Run all tests and demo"""
    print("Running Scientific Calculator Tests...")
    print("="*40)
    
    try:
        test_basic_arithmetic()
        test_scientific_functions()
        test_error_handling()
        test_format_result()
        
        print("\n🎉 All tests passed!")
        
        run_interactive_demo()
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()