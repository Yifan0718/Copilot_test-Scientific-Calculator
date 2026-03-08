#!/usr/bin/env python3
"""
Scientific Calculator
A comprehensive scientific calculator mimicking Casio FX991 functionality
Compatible with Windows and Linux platforms
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
import re


class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("科学计算器")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Calculator state
        self.current = "0"
        self.previous = ""
        self.operation = ""
        self.angle_mode = "deg"  # deg or rad
        self.memory = 0
        self.last_result = 0
        
        # Create GUI
        self.create_display()
        self.create_mode_frame()
        self.create_buttons()
        
        # Bind keyboard events
        self.root.bind('<Key>', self.on_key_press)
        self.root.focus_set()
        
    def create_display(self):
        """Create the calculator display"""
        display_frame = tk.Frame(self.root, bg='black', bd=2, relief='sunken')
        display_frame.pack(fill='x', padx=5, pady=5)
        
        # Main display
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Label(
            display_frame, 
            textvariable=self.display_var,
            font=('Arial', 16, 'bold'),
            bg='black', 
            fg='white',
            anchor='e',
            height=2
        )
        self.display.pack(fill='x', padx=5, pady=5)
        
        # Secondary display for operations
        self.operation_var = tk.StringVar(value="")
        self.operation_display = tk.Label(
            display_frame,
            textvariable=self.operation_var,
            font=('Arial', 10),
            bg='black',
            fg='yellow',
            anchor='e'
        )
        self.operation_display.pack(fill='x', padx=5)
        
    def create_mode_frame(self):
        """Create mode indicators"""
        mode_frame = tk.Frame(self.root)
        mode_frame.pack(fill='x', padx=5)
        
        self.angle_var = tk.StringVar(value="DEG")
        angle_label = tk.Label(mode_frame, textvariable=self.angle_var, 
                              font=('Arial', 10, 'bold'), fg='red')
        angle_label.pack(side='left')
        
        self.memory_var = tk.StringVar(value="")
        memory_label = tk.Label(mode_frame, textvariable=self.memory_var,
                               font=('Arial', 10, 'bold'), fg='blue')
        memory_label.pack(side='right')
        
    def create_buttons(self):
        """Create calculator buttons"""
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Button configuration
        btn_config = {
            'font': ('Arial', 10, 'bold'),
            'width': 6,
            'height': 2
        }
        
        # Scientific function buttons (row 0)
        scientific_buttons = [
            ("2nd", self.second_function, {'bg': 'lightblue'}),
            ("π", lambda: self.enter_constant('π'), {'bg': 'lightgreen'}),
            ("e", lambda: self.enter_constant('e'), {'bg': 'lightgreen'}),
            ("C", self.clear_all, {'bg': 'red', 'fg': 'white'}),
            ("⌫", self.backspace, {'bg': 'orange'})
        ]
        
        for i, (text, command, config) in enumerate(scientific_buttons):
            btn = tk.Button(button_frame, text=text, command=command, **btn_config, **config)
            btn.grid(row=0, column=i, padx=1, pady=1, sticky='nsew')
            
        # Advanced functions (row 1)
        advanced_buttons = [
            ("x²", lambda: self.function_operation('square'), {'bg': 'lightcyan'}),
            ("√", lambda: self.function_operation('sqrt'), {'bg': 'lightcyan'}),
            ("xʸ", lambda: self.binary_operation('**'), {'bg': 'lightcyan'}),
            ("log", lambda: self.function_operation('log'), {'bg': 'lightcyan'}),
            ("ln", lambda: self.function_operation('ln'), {'bg': 'lightcyan'})
        ]
        
        for i, (text, command, config) in enumerate(advanced_buttons):
            btn = tk.Button(button_frame, text=text, command=command, **btn_config, **config)
            btn.grid(row=1, column=i, padx=1, pady=1, sticky='nsew')
            
        # Trigonometric functions (row 2)
        trig_buttons = [
            ("sin", lambda: self.function_operation('sin'), {'bg': 'lightyellow'}),
            ("cos", lambda: self.function_operation('cos'), {'bg': 'lightyellow'}),
            ("tan", lambda: self.function_operation('tan'), {'bg': 'lightyellow'}),
            ("DEG/RAD", self.toggle_angle_mode, {'bg': 'pink'}),
            ("1/x", lambda: self.function_operation('reciprocal'), {'bg': 'lightcyan'})
        ]
        
        for i, (text, command, config) in enumerate(trig_buttons):
            btn = tk.Button(button_frame, text=text, command=command, **btn_config, **config)
            btn.grid(row=2, column=i, padx=1, pady=1, sticky='nsew')
            
        # Memory and special functions (row 3)
        memory_buttons = [
            ("MC", self.memory_clear, {'bg': 'lightsteelblue'}),
            ("MR", self.memory_recall, {'bg': 'lightsteelblue'}),
            ("M+", self.memory_add, {'bg': 'lightsteelblue'}),
            ("M-", self.memory_subtract, {'bg': 'lightsteelblue'}),
            ("n!", lambda: self.function_operation('factorial'), {'bg': 'lightcyan'})
        ]
        
        for i, (text, command, config) in enumerate(memory_buttons):
            btn = tk.Button(button_frame, text=text, command=command, **btn_config, **config)
            btn.grid(row=3, column=i, padx=1, pady=1, sticky='nsew')
            
        # Number and operation buttons
        # Row 4: 7, 8, 9, /, (
        row4_buttons = [
            ("7", lambda: self.enter_number('7')),
            ("8", lambda: self.enter_number('8')),
            ("9", lambda: self.enter_number('9')),
            ("÷", lambda: self.binary_operation('/')),
            ("(", lambda: self.enter_number('('))
        ]
        
        for i, (text, command, *config) in enumerate(row4_buttons):
            btn_conf = btn_config.copy()
            if text == "÷":
                btn_conf.update({'bg': 'lightcoral'})
            btn = tk.Button(button_frame, text=text, command=command, **btn_conf)
            btn.grid(row=4, column=i, padx=1, pady=1, sticky='nsew')
            
        # Row 5: 4, 5, 6, *, )
        row5_buttons = [
            ("4", lambda: self.enter_number('4')),
            ("5", lambda: self.enter_number('5')),
            ("6", lambda: self.enter_number('6')),
            ("×", lambda: self.binary_operation('*')),
            (")", lambda: self.enter_number(')'))
        ]
        
        for i, (text, command, *config) in enumerate(row5_buttons):
            btn_conf = btn_config.copy()
            if text == "×":
                btn_conf.update({'bg': 'lightcoral'})
            btn = tk.Button(button_frame, text=text, command=command, **btn_conf)
            btn.grid(row=5, column=i, padx=1, pady=1, sticky='nsew')
            
        # Row 6: 1, 2, 3, -, %
        row6_buttons = [
            ("1", lambda: self.enter_number('1')),
            ("2", lambda: self.enter_number('2')),
            ("3", lambda: self.enter_number('3')),
            ("−", lambda: self.binary_operation('-')),
            ("%", lambda: self.binary_operation('%'))
        ]
        
        for i, (text, command, *config) in enumerate(row6_buttons):
            btn_conf = btn_config.copy()
            if text in ["−", "%"]:
                btn_conf.update({'bg': 'lightcoral'})
            btn = tk.Button(button_frame, text=text, command=command, **btn_conf)
            btn.grid(row=6, column=i, padx=1, pady=1, sticky='nsew')
            
        # Row 7: 0, ., +/-, +, =
        row7_buttons = [
            ("0", lambda: self.enter_number('0')),
            (".", lambda: self.enter_number('.')),
            ("±", self.toggle_sign),
            ("+", lambda: self.binary_operation('+')),
            ("=", self.calculate)
        ]
        
        for i, (text, command, *config) in enumerate(row7_buttons):
            btn_conf = btn_config.copy()
            if text == "+":
                btn_conf.update({'bg': 'lightcoral'})
            elif text == "=":
                btn_conf.update({'bg': 'green', 'fg': 'white'})
            btn = tk.Button(button_frame, text=text, command=command, **btn_conf)
            btn.grid(row=7, column=i, padx=1, pady=1, sticky='nsew')
            
        # Configure grid weights
        for i in range(8):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            button_frame.grid_columnconfigure(i, weight=1)
            
    def update_display(self):
        """Update the calculator display"""
        self.display_var.set(self.current)
        
    def update_memory_display(self):
        """Update memory indicator"""
        if self.memory != 0:
            self.memory_var.set("M")
        else:
            self.memory_var.set("")
            
    def enter_number(self, num):
        """Handle number and decimal point input"""
        if self.current == "0" and num != ".":
            self.current = num
        elif num == "." and "." in self.current:
            return  # Prevent multiple decimal points
        else:
            self.current += num
        self.update_display()
        
    def enter_constant(self, constant):
        """Enter mathematical constants"""
        if constant == 'π':
            value = str(math.pi)
        elif constant == 'e':
            value = str(math.e)
        else:
            return
            
        if self.current == "0":
            self.current = value
        else:
            self.current += value
        self.update_display()
        
    def binary_operation(self, op):
        """Handle binary operations (+, -, *, /, **, %)"""
        if self.operation and self.previous:
            self.calculate()
        self.previous = self.current
        self.current = "0"
        self.operation = op
        self.operation_var.set(f"{self.previous} {op}")
        
    def function_operation(self, func):
        """Handle unary function operations"""
        try:
            value = float(self.current)
            
            if func == 'sin':
                if self.angle_mode == 'deg':
                    result = math.sin(math.radians(value))
                else:
                    result = math.sin(value)
            elif func == 'cos':
                if self.angle_mode == 'deg':
                    result = math.cos(math.radians(value))
                else:
                    result = math.cos(value)
            elif func == 'tan':
                if self.angle_mode == 'deg':
                    result = math.tan(math.radians(value))
                else:
                    result = math.tan(value)
            elif func == 'log':
                if value <= 0:
                    raise ValueError("Invalid input for log")
                result = math.log10(value)
            elif func == 'ln':
                if value <= 0:
                    raise ValueError("Invalid input for ln")
                result = math.log(value)
            elif func == 'sqrt':
                if value < 0:
                    raise ValueError("Invalid input for sqrt")
                result = math.sqrt(value)
            elif func == 'square':
                result = value ** 2
            elif func == 'reciprocal':
                if value == 0:
                    raise ValueError("Division by zero")
                result = 1 / value
            elif func == 'factorial':
                if value < 0 or value != int(value):
                    raise ValueError("Invalid input for factorial")
                result = math.factorial(int(value))
            else:
                return
                
            self.current = self.format_result(result)
            self.last_result = result
            self.update_display()
            
        except (ValueError, OverflowError) as e:
            messagebox.showerror("Error", f"Math Error: {str(e)}")
            self.current = "0"
            self.update_display()
            
    def calculate(self):
        """Perform calculation"""
        if not self.operation or not self.previous:
            return
            
        try:
            prev_val = float(self.previous)
            curr_val = float(self.current)
            
            if self.operation == '+':
                result = prev_val + curr_val
            elif self.operation == '-':
                result = prev_val - curr_val
            elif self.operation == '*':
                result = prev_val * curr_val
            elif self.operation == '/':
                if curr_val == 0:
                    raise ValueError("Division by zero")
                result = prev_val / curr_val
            elif self.operation == '**':
                result = prev_val ** curr_val
            elif self.operation == '%':
                result = prev_val % curr_val
            else:
                return
                
            self.current = self.format_result(result)
            self.last_result = result
            self.previous = ""
            self.operation = ""
            self.operation_var.set("")
            self.update_display()
            
        except (ValueError, OverflowError, ZeroDivisionError) as e:
            messagebox.showerror("Error", f"Math Error: {str(e)}")
            self.clear_all()
            
    def format_result(self, result):
        """Format calculation result"""
        if abs(result) > 1e10 or (abs(result) < 1e-10 and result != 0):
            return f"{result:.6e}"
        elif result == int(result):
            return str(int(result))
        else:
            return f"{result:.10g}"
            
    def clear_all(self):
        """Clear all calculator state"""
        self.current = "0"
        self.previous = ""
        self.operation = ""
        self.operation_var.set("")
        self.update_display()
        
    def backspace(self):
        """Remove last character"""
        if len(self.current) > 1:
            self.current = self.current[:-1]
        else:
            self.current = "0"
        self.update_display()
        
    def toggle_sign(self):
        """Toggle positive/negative sign"""
        if self.current != "0":
            if self.current.startswith('-'):
                self.current = self.current[1:]
            else:
                self.current = '-' + self.current
            self.update_display()
            
    def toggle_angle_mode(self):
        """Toggle between degree and radian mode"""
        if self.angle_mode == 'deg':
            self.angle_mode = 'rad'
            self.angle_var.set("RAD")
        else:
            self.angle_mode = 'deg'
            self.angle_var.set("DEG")
            
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        self.update_memory_display()
        
    def memory_recall(self):
        """Recall value from memory"""
        self.current = self.format_result(self.memory)
        self.update_display()
        
    def memory_add(self):
        """Add current value to memory"""
        try:
            self.memory += float(self.current)
            self.update_memory_display()
        except ValueError:
            pass
            
    def memory_subtract(self):
        """Subtract current value from memory"""
        try:
            self.memory -= float(self.current)
            self.update_memory_display()
        except ValueError:
            pass
            
    def second_function(self):
        """Handle second function button (placeholder for future expansion)"""
        messagebox.showinfo("Info", "Second function mode (asin, acos, atan, etc.) - Future feature")
        
    def on_key_press(self, event):
        """Handle keyboard input"""
        key = event.char
        
        if key.isdigit():
            self.enter_number(key)
        elif key == '.':
            self.enter_number('.')
        elif key == '+':
            self.binary_operation('+')
        elif key == '-':
            self.binary_operation('-')
        elif key == '*':
            self.binary_operation('*')
        elif key == '/':
            self.binary_operation('/')
        elif key == '%':
            self.binary_operation('%')
        elif key == '=':
            self.calculate()
        elif event.keysym == 'Return':
            self.calculate()
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif event.keysym == 'Escape':
            self.clear_all()
        elif key == '(':
            self.enter_number('(')
        elif key == ')':
            self.enter_number(')')


def main():
    """Main function to run the calculator"""
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    root.mainloop()


if __name__ == "__main__":
    main()