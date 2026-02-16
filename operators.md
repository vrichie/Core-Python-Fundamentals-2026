# Operators in Python

## Overview

Operators are special symbols that perform operations on variables and values. Python has several categories of operators.

---

## Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `6 / 2` | `3.0` |
| `%` | Modulus (Remainder) | `7 % 3` | `1` |
| `**` | Exponentiation (Power) | `2 ** 3` | `8` |
| `//` | Floor Division | `7 // 2` | `3` |

### Basic Examples

```python
a = 50
b = 4

# Addition
print(a + b)    # 54

# Subtraction
print(a - b)    # 46

# Multiplication
print(a * b)    # 200

# Division (returns float)
print(a / b)    # 12.5

# Floor Division (returns integer, rounds down)
print(a // b)   # 12

# Modulus (remainder after division)
print(a % b)    # 2

# Exponentiation
print(a ** b)   # 390625 (50 to the power of 4)
```

### Real-World Use Cases

```python
# Calculate total price with tax
item_price = 25.99
tax_rate = 0.08
total = item_price + (item_price * tax_rate)
print(f"Total: ${total:.2f}")  # Total: $28.07

# Calculate average of numbers
test_scores = [85, 90, 88, 92]
average = sum(test_scores) / len(test_scores)
print(f"Average: {average}")  # Average: 88.75

# Check if a number is even or odd
number = 17
if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")  # Odd number

# Calculate compound interest
principal = 1000
rate = 0.05
years = 2
amount = principal * (1 + rate) ** years
print(f"Amount: ${amount:.2f}")  # Amount: $1102.50

# Get hours and minutes from total minutes
total_minutes = 125
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"Time: {hours}h {minutes}m")  # Time: 2h 5m
```

---

## Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Example | Equivalent To |
|----------|---------|---------------|
| `=` | `x = 5` | Assign |
| `+=` | `x += 3` | `x = x + 3` |
| `-=` | `x -= 3` | `x = x - 3` |
| `*=` | `x *= 3` | `x = x * 3` |
| `/=` | `x /= 3` | `x = x / 3` |
| `%=` | `x %= 3` | `x = x % 3` |
| `**=` | `x **= 3` | `x = x ** 3` |
| `//=` | `x //= 3` | `x = x // 3` |

### Basic Examples

```python
a = 50
b = 4

# Regular assignment
a = 10

# Add and assign
a += 5      # a = a + 5 → a = 15

# Subtract and assign
a -= 3      # a = a - 3 → a = 12

# Multiply and assign
a *= 2      # a = a * 2 → a = 24

# Divide and assign
a /= 4      # a = a / 4 → a = 6.0

# Floor divide and assign
a //= 2     # a = a // 2 → a = 3

# Modulus and assign
a %= 2      # a = a % 2 → a = 1

# Exponentiation and assign
a = 2
a **= 3     # a = a ** 3 → a = 8
```

### Real-World Use Cases

```python
# Accumulating a total
total = 0
total += 10   # total = 10
total += 25   # total = 35
total += 15   # total = 50
print(f"Total: ${total}")  # Total: $50

# Modifying quantities
stock = 100
stock -= 5    # Sold 5 items
stock -= 10   # Sold 10 more items
print(f"Stock remaining: {stock}")  # Stock remaining: 85

# Scaling values
height = 170  # cm
height *= 2   # Now representing in different units
print(f"Height: {height} cm")  # Height: 340 cm

# Reducing precision
percentage = 95.7654
percentage //= 1  # Get integer percentage
print(f"Percentage: {percentage}%")

# Building strings (concatenation)
message = "Hello"
message += " "
message += "World"
print(message)  # Hello World

# Incrementing a counter
counter = 0
counter += 1   # counter = 1
counter += 1   # counter = 2
counter += 1   # counter = 3
print(f"Counter: {counter}")  # Counter: 3
```

---

## Comparison Operators

Comparison operators are used to compare two values and return a Boolean value (`True` or `False`).

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 3` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `5 <= 3` | `False` |

### Basic Examples

```python
a = 50
b = 4

# Equal to
print(a == b)   # False (50 is not equal to 4)
print(a == 50)  # True (50 equals 50)

# Not equal to
print(a != b)   # True (50 is not equal to 4)
print(a != 50)  # False (50 equals 50, so not different)

# Greater than
print(a > b)    # True (50 is greater than 4)
print(b > a)    # False (4 is not greater than 50)

# Less than
print(a < b)    # False (50 is not less than 4)
print(b < a)    # True (4 is less than 50)

# Greater than or equal to
print(a >= b)   # True (50 is greater than 4)
print(a >= 50)  # True (50 equals 50)

# Less than or equal to
print(a <= b)   # False (50 is not less than or equal to 4)
print(b <= 50)  # True (4 is less than 50)
```

### Comparing Strings

```python
# Alphabetical comparison
print("apple" == "apple")      # True
print("apple" != "orange")     # True
print("apple" < "banana")      # True (alphabetically)
print("zebra" > "apple")       # True (alphabetically)

# Case matters
print("Apple" == "apple")      # False (different cases)
```

### Comparing Floats and Integers

```python
print(5 == 5.0)     # True (Python treats them as equal)
print(5 < 5.5)      # True
print(3.14 > 3)     # True
```

### Real-World Use Cases

```python
# Age verification
age = 25
min_age = 18
if age >= min_age:
    print("You are old enough to vote")
else:
    print("You are too young to vote")

# Grade checking
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Password validation
password = "myPassword123"
min_length = 8
if len(password) >= min_length:
    print("Password is strong enough")
else:
    print("Password is too short")

# Balance checking
account_balance = 150.50
withdrawal = 100
if account_balance >= withdrawal:
    account_balance -= withdrawal
    print(f"Withdrawal successful. New balance: ${account_balance:.2f}")
else:
    print("Insufficient funds")

# Checking equality
user_input = input("Enter the secret code: ")
correct_code = "python123"
if user_input == correct_code:
    print("Access granted!")
else:
    print("Access denied!")

# Temperature comparison
current_temp = 28
freezing = 0
boiling = 100
if current_temp < freezing:
    print("It's freezing!")
elif current_temp > boiling:
    print("It's boiling!")
else:
    print("Temperature is moderate")

# Range checking
score = 75
if score >= 50 and score <= 100:
    print("You passed the exam")
else:
    print("You failed the exam")
```

### Chaining Comparisons

Python allows you to chain comparisons naturally:

```python
# Check if a value is between two numbers
x = 50
if 0 < x < 100:
    print("x is between 0 and 100")

# More complex chains
y = 75
if 0 <= y <= 100:
    print("y is in valid range")

# Age in valid ranges
age = 25
if 18 <= age < 65:
    print("You are in the working age group")
```

---

## Summary

- **Arithmetic Operators**: Perform mathematical calculations (+, -, *, /, %, **, //)
- **Assignment Operators**: Assign values and modify variables (=, +=, -=, *=, /=, etc.)
- **Comparison Operators**: Compare values and return True/False (==, !=, >, <, >=, <=)

Next: Learn about **Logical Operators** (and, or, not) to combine multiple conditions!
