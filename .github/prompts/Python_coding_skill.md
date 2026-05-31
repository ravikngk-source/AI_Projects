# Python Development Skill

## Purpose

Generate clean, maintainable, reusable, and production-ready Python code following Python best practices and coding standards.

---

# Core Principles

1. Prioritize readability over complexity.
2. Follow Pythonic coding standards.
3. Avoid duplicate code and logic.
4. Create reusable and maintainable solutions.
5. Generate self-documenting code.
6. Ensure code is easy to debug and extend.

---

# Naming Standards

Use descriptive and meaningful names.

## File Names

Use snake_case.

Examples:

```python
calculator.py
user_service.py
data_validator.py
```

Avoid:

```python
calc.py
test1.py
temp.py
```

---

## Class Names

Use PascalCase.

Examples:

```python
Calculator
UserService
DataValidator
```

---

## Method Names

Use descriptive snake_case.

Examples:

```python
calculate_total_price()
validate_customer_record()
generate_report()
```

Avoid:

```python
run()
process()
execute()
```

unless the purpose is obvious.

---

## Variable Names

Use meaningful names.

Examples:

```python
customer_name
total_amount
validation_result
```

Avoid:

```python
x
a
temp
```

except for simple loops.

---

# Documentation Standards

Every class and method must contain meaningful docstrings.

## Class Example

```python
class Calculator:
    """
    Provides mathematical operations.
    """
```

## Method Example

```python
def add_numbers(self, first_number, second_number):
    """
    Add two numbers and return the result.

    Args:
        first_number: First value.
        second_number: Second value.

    Returns:
        Sum of both numbers.
    """
```

---

# Code Reusability Standards

Before creating new logic:

1. Check whether similar functionality already exists.
2. Reuse existing methods whenever possible.
3. Avoid copy-paste implementations.
4. Extract common logic into reusable methods.

---

# Error Handling Standards

Use meaningful exception handling.

Preferred:

```python
try:
    process_data()
except ValueError as error:
    print(error)
```

Avoid:

```python
except:
    pass
```

---

# Code Quality Checklist

Before generating code verify:

✓ Descriptive naming used

✓ No duplicate logic

✓ Proper docstrings added

✓ Python coding standards followed

✓ Reusable implementation created

✓ Error handling included where applicable

✓ Code is easy to understand

---

# Expected Outcome

Generate Python code that is:

* Readable
* Reusable
* Maintainable
* Scalable
* Well documented
* Beginner friendly
* Production ready
