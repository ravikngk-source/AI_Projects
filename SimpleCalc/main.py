"""
Command-line interface for the simple calculator application.
"""

from calculator import Calculator


def display_menu():
    """Display the calculator menu options."""
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("========================")


def get_user_input():
    """
    Prompt user for two numbers and operation choice.

    Returns:
        Tuple of (first_number, second_number, choice) or None if exit selected.
    """
    try:
        choice = input("\nSelect operation (1-5): ").strip()
        
        if choice == "5":
            return None
        
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select 1-5.")
            return None
        
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        
        return first_number, second_number, choice
    
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return None


def execute_operation(calculator, first_number, second_number, choice):
    """
    Execute the selected operation and display result.

    Args:
        calculator: Calculator instance.
        first_number: First numeric operand.
        second_number: Second numeric operand.
        choice: User's operation selection.
    """
    try:
        if choice == "1":
            result = calculator.add(first_number, second_number)
            print(f"\nResult: {first_number} + {second_number} = {result}")
        elif choice == "2":
            result = calculator.subtract(first_number, second_number)
            print(f"\nResult: {first_number} - {second_number} = {result}")
        elif choice == "3":
            result = calculator.multiply(first_number, second_number)
            print(f"\nResult: {first_number} × {second_number} = {result}")
        elif choice == "4":
            result = calculator.divide(first_number, second_number)
            print(f"\nResult: {first_number} ÷ {second_number} = {result}")
    
    except (TypeError, ZeroDivisionError) as error:
        print(f"\nError: {error}")


def main():
    """Run the calculator application."""
    calculator = Calculator()
    
    print("Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        user_input = get_user_input()
        
        if user_input is None and input("Enter '5' again to exit or press Enter to continue: ").strip() != "5":
            continue
        elif user_input is None:
            break
        
        first_number, second_number, choice = user_input
        execute_operation(calculator, first_number, second_number, choice)
    
    print("\nThank you for using Simple Calculator. Goodbye!")


if __name__ == "__main__":
    main()
