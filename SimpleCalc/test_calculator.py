"""
Unit tests for the calculator module.
"""

import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    """Create a calculator instance for testing."""
    return Calculator()


class TestCalculatorAddition:
    """Test cases for addition operation."""

    def test_add_positive_numbers(self, calculator):
        """Test adding two positive numbers."""
        assert calculator.add(5, 3) == 8

    def test_add_negative_numbers(self, calculator):
        """Test adding two negative numbers."""
        assert calculator.add(-5, -3) == -8

    def test_add_mixed_numbers(self, calculator):
        """Test adding positive and negative numbers."""
        assert calculator.add(5, -3) == 2

    def test_add_floats(self, calculator):
        """Test adding floating-point numbers."""
        assert calculator.add(2.5, 3.5) == 6.0


class TestCalculatorSubtraction:
    """Test cases for subtraction operation."""

    def test_subtract_positive_numbers(self, calculator):
        """Test subtracting two positive numbers."""
        assert calculator.subtract(5, 3) == 2

    def test_subtract_negative_numbers(self, calculator):
        """Test subtracting two negative numbers."""
        assert calculator.subtract(-5, -3) == -2

    def test_subtract_floats(self, calculator):
        """Test subtracting floating-point numbers."""
        assert calculator.subtract(5.5, 2.5) == 3.0


class TestCalculatorMultiplication:
    """Test cases for multiplication operation."""

    def test_multiply_positive_numbers(self, calculator):
        """Test multiplying two positive numbers."""
        assert calculator.multiply(5, 3) == 15

    def test_multiply_by_zero(self, calculator):
        """Test multiplying by zero."""
        assert calculator.multiply(5, 0) == 0

    def test_multiply_negative_numbers(self, calculator):
        """Test multiplying negative numbers."""
        assert calculator.multiply(-5, 3) == -15

    def test_multiply_floats(self, calculator):
        """Test multiplying floating-point numbers."""
        assert calculator.multiply(2.5, 4.0) == 10.0


class TestCalculatorDivision:
    """Test cases for division operation."""

    def test_divide_positive_numbers(self, calculator):
        """Test dividing two positive numbers."""
        assert calculator.divide(10, 2) == 5.0

    def test_divide_with_remainder(self, calculator):
        """Test division with decimal result."""
        assert calculator.divide(7, 2) == 3.5

    def test_divide_negative_numbers(self, calculator):
        """Test dividing negative numbers."""
        assert calculator.divide(-10, 2) == -5.0

    def test_divide_by_zero(self, calculator):
        """Test division by zero raises error."""
        with pytest.raises(ZeroDivisionError):
            calculator.divide(10, 0)


class TestCalculatorErrorHandling:
    """Test cases for error handling."""

    def test_add_non_numeric_first_argument(self, calculator):
        """Test addition with non-numeric first argument."""
        with pytest.raises(TypeError):
            calculator.add("5", 3)

    def test_add_non_numeric_second_argument(self, calculator):
        """Test addition with non-numeric second argument."""
        with pytest.raises(TypeError):
            calculator.add(5, "3")

    def test_subtract_non_numeric_arguments(self, calculator):
        """Test subtraction with non-numeric arguments."""
        with pytest.raises(TypeError):
            calculator.subtract("5", 3)

    def test_multiply_non_numeric_arguments(self, calculator):
        """Test multiplication with non-numeric arguments."""
        with pytest.raises(TypeError):
            calculator.multiply(5, None)

    def test_divide_non_numeric_arguments(self, calculator):
        """Test division with non-numeric arguments."""
        with pytest.raises(TypeError):
            calculator.divide(10, "2")
