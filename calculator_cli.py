#!/usr/bin/env python3
"""
Command Line Scientific Calculator
A command-line interface for the scientific calculator
Compatible with environments without GUI support
"""

import math
import re
import sys


class CommandLineCalculator:
    """Command-line scientific calculator"""
    
    def __init__(self):
        self.angle_mode = "deg"  # deg or rad
        self.memory = 0
        self.last_result = 0
        
    def display_welcome(self):
        """Display welcome message and help"""
        print("="*60)
        print("🧮 SCIENTIFIC CALCULATOR (Command Line Version)")
        print("="*60)
        print("Type mathematical expressions or use commands:")
        print("\nBasic Operations:")
        print("  +, -, *, /, ** (power), % (modulo)")
        print("  Examples: 2+3, 5*6, 2**3, 17%5")
        print("\nScientific Functions:")
        print("  sin(x), cos(x), tan(x)  - Trigonometric functions")
        print("  sqrt(x), log(x), ln(x)  - Square root, log₁₀, natural log")
        print("  fact(x)                 - Factorial")
        print("  Examples: sin(30), sqrt(16), log(100)")
        print("\nConstants:")
        print("  pi, e")
        print("\nCommands:")
        print("  deg/rad    - Switch angle mode")
        print("  mc/mr/m+/m- - Memory clear/recall/add/subtract")
        print("  help       - Show this help")
        print("  quit/exit  - Exit calculator")
        print("\nCurrent mode: {} | Memory: {}".format(
            self.angle_mode.upper(), 
            "Empty" if self.memory == 0 else f"{self.memory}"
        ))
        print("="*60)
        
    def parse_expression(self, expr):
        """Parse and evaluate mathematical expression"""
        # Remove spaces
        expr = expr.replace(' ', '')
        
        # Replace constants
        expr = expr.replace('pi', str(math.pi))
        expr = expr.replace('e', str(math.e))
        
        # Replace functions with Python equivalents
        if self.angle_mode == 'deg':
            # Convert degree functions to radians
            expr = re.sub(r'sin\(([^)]+)\)', 
                         lambda m: f'math.sin(math.radians({m.group(1)}))', expr)
            expr = re.sub(r'cos\(([^)]+)\)', 
                         lambda m: f'math.cos(math.radians({m.group(1)}))', expr)
            expr = re.sub(r'tan\(([^)]+)\)', 
                         lambda m: f'math.tan(math.radians({m.group(1)}))', expr)
        else:
            expr = re.sub(r'sin\(([^)]+)\)', r'math.sin(\1)', expr)
            expr = re.sub(r'cos\(([^)]+)\)', r'math.cos(\1)', expr)
            expr = re.sub(r'tan\(([^)]+)\)', r'math.tan(\1)', expr)
            
        # Replace other functions
        expr = re.sub(r'sqrt\(([^)]+)\)', r'math.sqrt(\1)', expr)
        expr = re.sub(r'log\(([^)]+)\)', r'math.log10(\1)', expr)
        expr = re.sub(r'ln\(([^)]+)\)', r'math.log(\1)', expr)
        expr = re.sub(r'fact\(([^)]+)\)', r'math.factorial(int(\1))', expr)
        
        return expr
        
    def evaluate(self, expr):
        """Safely evaluate mathematical expression"""
        try:
            # Parse the expression
            parsed_expr = self.parse_expression(expr)
            
            # Create safe evaluation environment
            safe_dict = {
                "__builtins__": {},
                "math": math,
                "abs": abs,
                "int": int,
                "float": float,
                "ans": self.last_result
            }
            
            # Evaluate expression
            result = eval(parsed_expr, safe_dict)
            self.last_result = result
            
            return self.format_result(result)
            
        except ZeroDivisionError:
            return "Error: Division by zero"
        except ValueError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"Error: Invalid expression ({str(e)})"
            
    def format_result(self, result):
        """Format calculation result"""
        if isinstance(result, complex):
            return str(result)
        elif abs(result) > 1e10 or (abs(result) < 1e-10 and result != 0):
            return f"{result:.6e}"
        elif result == int(result):
            return str(int(result))
        else:
            return f"{result:.10g}"
            
    def handle_command(self, cmd):
        """Handle calculator commands"""
        cmd = cmd.lower().strip()
        
        if cmd in ['deg', 'rad']:
            self.angle_mode = cmd
            return f"Angle mode set to {cmd.upper()}"
        elif cmd == 'mc':
            self.memory = 0
            return "Memory cleared"
        elif cmd == 'mr':
            return f"Memory recall: {self.format_result(self.memory)}"
        elif cmd.startswith('m+'):
            try:
                value = float(cmd[2:]) if len(cmd) > 2 else self.last_result
                self.memory += value
                return f"Added {value} to memory. Memory: {self.format_result(self.memory)}"
            except ValueError:
                return "Error: Invalid value for M+"
        elif cmd.startswith('m-'):
            try:
                value = float(cmd[2:]) if len(cmd) > 2 else self.last_result
                self.memory -= value
                return f"Subtracted {value} from memory. Memory: {self.format_result(self.memory)}"
            except ValueError:
                return "Error: Invalid value for M-"
        elif cmd == 'help':
            self.display_welcome()
            return ""
        else:
            return "Unknown command. Type 'help' for available commands."
            
    def run(self):
        """Run the calculator interactive loop"""
        self.display_welcome()
        
        print("\nEnter expressions or commands (type 'help' for help, 'quit' to exit):")
        
        while True:
            try:
                # Get user input
                user_input = input(f"\n[{self.angle_mode.upper()}] calc> ").strip()
                
                # Check for exit commands
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Thank you for using the Scientific Calculator!")
                    break
                    
                # Skip empty input
                if not user_input:
                    continue
                    
                # Handle commands
                if user_input.lower() in ['deg', 'rad', 'mc', 'mr', 'help'] or \
                   user_input.lower().startswith('m+') or user_input.lower().startswith('m-'):
                    result = self.handle_command(user_input)
                    if result:
                        print(result)
                else:
                    # Evaluate mathematical expression
                    result = self.evaluate(user_input)
                    print(f"= {result}")
                    
            except KeyboardInterrupt:
                print("\n\nThank you for using the Scientific Calculator!")
                break
            except EOFError:
                print("\n\nThank you for using the Scientific Calculator!")
                break


def main():
    """Main function"""
    calculator = CommandLineCalculator()
    calculator.run()


if __name__ == "__main__":
    main()