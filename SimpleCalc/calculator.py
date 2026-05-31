"""
Simple calculator module providing basic mathematical operations.
"""


class Calculator:
    """
    Provides fundamental mathematical operations.
    
    Supports addition, subtraction, multiplication, and division
    with proper error handling for invalid operations.
    """

    def add(self, first_number, second_number):
        """
        Add two numbers and return the result.

        Args:
            first_number: First numeric value.
            second_number: Second numeric value.

        Returns:
            Sum of both numbers.

        Raises:
            TypeError: If arguments are not numeric.
        """
        if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
            raise TypeError("Both arguments must be numeric values.")
        return first_number + second_number

    def subtract(self, first_number, second_number):
        """
        Subtract second number from first number.

        Args:
            first_number: Numeric value to subtract from.
            second_number: Numeric value to subtract.

        Returns:
            Difference between the numbers.

        Raises:
            TypeError: If arguments are not numeric.
        """
        if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
            raise TypeError("Both arguments must be numeric values.")
        return first_number - second_number

    def multiply(self, first_number, second_number):
        """
        Multiply two numbers and return the result.

        Args:
            first_number: First numeric value.
            second_number: Second numeric value.

        Returns:
            Product of both numbers.

        Raises:
            TypeError: If arguments are not numeric.
        """
        if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
            raise TypeError("Both arguments must be numeric values.")
        return first_number * second_number

    def divide(self, first_number, second_number):
        """
        Divide first number by second number.

        Args:
            first_number: Numeric value to be divided.
            second_number: Numeric value to divide by.

        Returns:
            Quotient of the division.

        Raises:
            TypeError: If arguments are not numeric.
            ZeroDivisionError: If second_number is zero.
        """
        if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
            raise TypeError("Both arguments must be numeric values.")
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
