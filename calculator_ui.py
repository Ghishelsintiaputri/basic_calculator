"""
User interface for the calculator.
"""

from calculator import Calculator

class CalculatorUI:
    def __init__(self):
        self.calculator = Calculator()
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*40)
        print("          SIMPLE CALCULATOR")
        print("="*40)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. View History")
        print("7. Clear History")
        print("8. Exit")
        print("="*40)
    
    def get_number_input(self, prompt):
        """Get valid number input from user."""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    def perform_operation(self, choice):
        """Perform the selected arithmetic operation."""
        operations = {
            1: ("Addition", self.calculator.add),
            2: ("Subtraction", self.calculator.subtract),
            3: ("Multiplication", self.calculator.multiply),
            4: ("Division", self.calculator.divide),
            5: ("Power", self.calculator.power)
        }
        
        if choice not in operations:
            return
        
        operation_name, operation_func = operations[choice]
        
        print(f"\n--- {operation_name} ---")
        try:
            num1 = self.get_number_input("Enter first number: ")
            num2 = self.get_number_input("Enter second number: ")
            
            result = operation_func(num1, num2)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def run(self):
        """Main loop to run the calculator."""
        print("Welcome to the Simple Calculator!")
        
        while True:
            self.display_menu()
            
            try:
                choice = int(input("Enter your choice (1-8): "))
                
                if choice == 8:
                    print("Thank you for using the calculator! Goodbye!")
                    break
                elif choice == 6:
                    self.calculator.display_history()
                elif choice == 7:
                    self.calculator.clear_history()
                    print("History cleared!")
                elif 1 <= choice <= 5:
                    self.perform_operation(choice)
                else:
                    print("Invalid choice! Please select 1-8.")
                    
            except ValueError:
                print("Invalid input! Please enter a number between 1-8.")
            except KeyboardInterrupt:
                print("\n\nCalculator terminated by user. Goodbye!")
                break