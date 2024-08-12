"""
Main calculator module with arithmetic operations and history tracking.
"""

class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers and return result."""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract b from a and return result."""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers and return result."""
        result = a * b
        self._add_to_history(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide a by b and return result."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self._add_to_history(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        """Raise a to the power of b and return result."""
        result = a ** b
        self._add_to_history(f"{a} ^ {b} = {result}")
        return result
    
    def _add_to_history(self, operation):
        """Add operation to history."""
        self.history.append(operation)
    
    def get_history(self):
        """Return calculation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
    
    def display_history(self):
        """Display calculation history."""
        if not self.history:
            print("No history available.")
            return
        
        print("\n--- Calculation History ---")
        for i, operation in enumerate(self.history, 1):
            print(f"{i}. {operation}")
        print("---------------------------\n")