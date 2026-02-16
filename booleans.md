# Booleans in Python

## What is a Boolean?

A boolean is a data type that can only have two values: `True` or `False`. Booleans are fundamental in programming because they allow us to make decisions and control the flow of our programs.

## Boolean Values

```python
x = True
y = False

print(type(x))  # <class 'bool'>
print(type(y))  # <class 'bool'>
```

## The `bool()` Function

The `bool()` function converts any value to a boolean. Almost everything has a boolean value in Python.

### Values that evaluate to `False`:
- `False` itself
- `None`
- `0` (and `0.0`, `0j`)
- Empty sequences: `""`, `[]`, `()`, `{}`
- Empty dictionary: `{}`

### Values that evaluate to `True`:
- `True` itself
- Any non-zero number: `1`, `-5`, `3.14`
- Any non-empty string: `"hello"`, `"0"`
- Any non-empty sequence: `[1, 2]`, `(1,)`, `"hello"`
- Any non-empty dictionary: `{"key": "value"}`

## Examples

### Converting to Boolean
```python
print(bool(True))       # True
print(bool(False))      # False
print(bool(0))          # False
print(bool(1))          # True
print(bool(2))          # True
print(bool(-5))         # True
print(bool(3.14))       # True

print(bool(""))         # False (empty string)
print(bool("hello"))    # True (non-empty string)
print(bool("0"))        # True (string with content)

print(bool([]))         # False (empty list)
print(bool([1, 2]))     # True (non-empty list)
print(bool(["any"]))    # True (non-empty list)

print(bool(()))         # False (empty tuple)
print(bool((1,)))       # True (non-empty tuple)

print(bool({}))         # False (empty dictionary)
print(bool({"key": "value"}))  # True (non-empty dictionary)

print(bool(None))       # False
```

### Using `bool()` in Conditional Statements

```python
# Example 1: Checking if a list has items
x = ["any"]
if bool(x):
    print("The list has items")
else:
    print("The list is empty")

# Example 2: Checking age requirement
age = -10
min_age = 0
if bool(age > min_age):
    print("Old enough")
else:
    print("Not old enough")

# Example 3: Checking various values
password = ""
if bool(password):
    print("Password is set")
else:
    print("Password is empty")

# Example 4: Checking user input
user_input = 0
if bool(user_input):
    print("User provided input")
else:
    print("No input provided")
```

### Implicit Boolean Conversion

In Python, you often don't need to explicitly use `bool()` in conditionals. The if statement automatically converts values to boolean:

```python
# These are equivalent:
if bool(x):
    # do something

if x:
    # do something

# Example with numbers
count = 5
if count:  # Implicitly checks if count is True (non-zero)
    print("Count is non-zero")

# Example with strings
name = "John"
if name:  # Implicitly checks if name is True (non-empty)
    print(f"Name is: {name}")

# Example with lists
items = [1, 2, 3]
if items:  # Implicitly checks if list is non-empty
    print(f"You have {len(items)} items")
```

## Common Use Cases

### 1. Validating Non-Empty Data
```python
username = input("Enter username: ")
if username:  # Checks if not empty
    print(f"Welcome, {username}")
```

### 2. Checking if Container Has Items
```python
shopping_cart = []
if shopping_cart:
    print("Ready to checkout")
else:
    print("Your cart is empty")
```

### 3. Checking Conditions
```python
age = 25
min_age = 18
if age >= min_age:
    print("You can vote")
```

### 4. Checking for None (Null)
```python
value = None
if value is None:
    print("No value provided")
else:
    print(f"Value is: {value}")

# Or using boolean context
if not value:
    print("Value is falsy")
```

## Boolean Operators (Next Step)

We'll explore logical operators (`and`, `or`, `not`) that combine booleans in the next section!
