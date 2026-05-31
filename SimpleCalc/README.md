# Simple Calculator

A clean, maintainable command-line calculator application built with Python.

## Features

- **Basic Operations**: Add, subtract, multiply, and divide
- **Error Handling**: Proper validation and error messages
- **User-Friendly Interface**: Interactive CLI menu
- **Well-Tested**: Comprehensive unit tests included

## Project Structure

```
SimpleCalc/
├── calculator.py       # Core calculator logic
├── main.py            # CLI interface
├── test_calculator.py # Unit tests
└── README.md          # This file
```

## Installation

No external dependencies required. Python 3.6+ is needed.

For testing, install pytest:

```bash
pip install pytest
```

## Usage

Run the calculator:

```bash
python main.py
```

Follow the on-screen menu to:
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers
5. Exit

### Example

```
=== Simple Calculator ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
========================

Select operation (1-5): 1
Enter first number: 10
Enter second number: 5

Result: 10.0 + 5.0 = 15.0
```

## Running Tests

Execute all tests:

```bash
pytest test_calculator.py
```

Run with verbose output:

```bash
pytest test_calculator.py -v
```

## Code Quality

This project follows Python best practices:

- Descriptive naming conventions (PascalCase for classes, snake_case for functions)
- Comprehensive docstrings for all classes and methods
- Meaningful error handling with specific exceptions
- Clean, readable code prioritized over complexity
- Reusable components and no duplicate logic
