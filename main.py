"""
Main entry point for the Simple Calculator application.
"""

from calculator_ui import CalculatorUI

def main():
    """Start the calculator application"""
    try:
        ui = CalculatorUI()
        ui.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please restart the application.")

if __name__ == "__main__":
    main()