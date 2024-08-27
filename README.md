## Simple Calculator with History Tracking

### Overview
A Python-based simple calculator that performs basic arithmetic operations and maintains a history of all calculations performed during the session.

### Features
- **Basic Arithmetic Operations**: Addition, Subtraction, Multiplication, Division, and Power
- **History Tracking**: Keeps track of all calculations performed
- **User-Friendly Interface**: Simple text-based menu system
- **Error Handling**: Proper validation and error messages
- **Unit Tests**: Comprehensive test coverage

### Requirements
- Python 3.6 or higher

### Installation & Usage

1. **Save all files** in the same directory:
   - `calculator.py`
   - `calculator_ui.py`
   - `main.py`
   - `test_calculator.py` (optional - for testing)

2. **Run the calculator**:
   ```bash
   python main.py
   ```

3. **Follow the menu prompts**:
   - Select operations (1-5) for arithmetic calculations
   - Choose option 6 to view calculation history
   - Choose option 7 to clear history
   - Choose option 8 to exit

### Running Tests
To run the unit tests:
```bash
python test_calculator.py
```

### File Structure
- `calculator.py` - Core calculator logic and history management
- `calculator_ui.py` - User interface and menu handling
- `main.py` - Application entry point
- `test_calculator.py` - Unit tests for calculator functions

### Example Usage
```
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Power (^)
6. View History
7. Clear History
8. Exit

Enter your choice (1-8): 1

--- Addition ---
Enter first number: 10
Enter second number: 5
Result: 15.0
```

### Notes
- The calculator uses floating-point numbers for all operations
- History is maintained only for the current session (cleared when program exits)
- Division by zero is properly handled with error messages
- The application includes proper input validation