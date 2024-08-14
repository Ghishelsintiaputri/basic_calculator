"""
User interface for the calculator application.
"""

from calculator import Calculator

class CalculatorUI:
    def __init__(self):
        self.calc = Calculator()
    
    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "="*50)
        print("           SIMPLE CALCULATOR")
        print("="*50)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (×)")
        print("4. Division (÷)")
        print("5. Power (^)")
        print("6. View History")
        print("7. Clear History")
        print("8. Exit")
        print("="*50)
    
    def get_number_input(self, prompt):
        """Get valid number input from user"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    def perform_operation(self, choice):
        """Perform the selected arithmetic operation"""
        operations = {
            1: ("Addition", self.calc.add),
            2: ("Subtraction", self.calc.subtract),
            3: ("Multiplication", self.calc.multiply),
            4: ("Division", self.calc.divide),
            5: ("Power", self.calc.power)
        }
        
        if choice in operations:
            operation_name, operation_func = operations[choice]
            print(f"\n--- {operation_name} ---")
            
            try:
                a = self.get_number_input("Enter first number: ")
                b = self.get_number_input("Enter second number: ")
                
                result = operation_func(a, b)
                print(f"Result: {result}")
                
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
    
    def run(self):
        """Main application loop"""
        print("Welcome to the Simple Calculator!")
        
        while True:
            self.display_menu()
            
            try:
                choice = int(input("\nEnter your choice (1-8): "))
                
                if choice == 6:
                    self.calc.display_history()
                elif choice == 7:
                    self.calc.clear_history()
                    print("History cleared!")
                elif choice == 8:
                    print("Thank you for using the calculator. Goodbye!")
                    break
                elif 1 <= choice <= 5:
                    self.perform_operation(choice)
                else:
                    print("Invalid choice! Please select 1-8.")
                    
            except ValueError:
                print("Invalid input! Please enter a number between 1-8.")
            except KeyboardInterrupt:
                print("\n\nCalculator terminated by user. Goodbye!")
                break