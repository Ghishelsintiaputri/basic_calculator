## Simple Calculator with History Tracking

### Overview
A Python-based simple calculator that performs basic arithmetic operations and maintains a history of all calculations.

### Features
- **Basic Operations**: Addition, Subtraction, Multiplication, Division, Power
- **History Tracking**: Keeps track of all operations performed
- **User-Friendly Interface**: Simple text-based menu system
- **Error Handling**: Handles invalid inputs and division by zero
- **Unit Tests**: Comprehensive test coverage

### Files Structure
- `calculator.py` - Core calculator logic and history management
- `calculator_ui.py` - User interface and menu system
- `main.py` - Application entry point
- `test_calculator.py` - Unit tests for calculator functionality

### Requirements
- Python 3.6 or higher

### How to Use

1. **Run the Calculator**:
   ```bash
   python main.py
   ```

2. **Using the Menu**:
   - Select operations 1-5 for arithmetic calculations
   - Select 6 to view calculation history
   - Select 7 to clear history
   - Select 8 to exit

3. **Running Tests**:
   ```bash
   python -m unittest test_calculator.py
   ```
   or
   ```bash
   python test_calculator.py
   ```

### Example Usage
```
Enter your choice (1-8): 1
Enter first number: 10
Enter second number: 5
Result: 15.0

Enter your choice (1-8): 6
=== CALCULATION HISTORY ===
1. 10 + 5 = 15.0
===========================
```

### Error Handling
- Invalid number inputs are caught and prompt for re-entry
- Division by zero is prevented with clear error messages
- Invalid menu choices are handled gracefully

### Extending the Calculator
You can easily add new operations by:
1. Adding the method in `calculator.py`
2. Updating the menu in `calculator_ui.py`
3. Adding corresponding tests in `test_calculator.py`

The modular design makes it easy to maintain and extend functionality.