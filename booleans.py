# BOOLEANS IN PYTHON
# A boolean is True or False
# Used to make decisions in programs

print("\nBOOLEAN VALUES")
x = True
y = False
print(f"x = {x}")
print(f"y = {y}")

# VALUES THAT EVALUATE TO False
print("\nVALUES THAT ARE False:")
print(f"bool(False): {bool(False)}")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')} (empty string)")
print(f"bool([]): {bool([])} (empty list)")
print(f"bool(None): {bool(None)}")

# VALUES THAT EVALUATE TO True
print("\nVALUES THAT ARE True:")
print(f"bool(True): {bool(True)}")
print(f"bool(1): {bool(1)}")
print(f"bool(42): {bool(42)}")
print(f"bool('hello'): {bool('hello')} (non-empty string)")
print(f"bool([1, 2, 3]): {bool([1, 2, 3])} (non-empty list)")

# USING bool() IN CONDITIONS
print("\nUSING BOOLEANS IN IF STATEMENTS")

# Example 1: Check if list has items
x = ["any"]
if bool(x):
    print("List has items")
else:
    print("List is empty")

# Example 2: Check age
age = 25
if age >= 18:
    print(f"Age {age}: Can vote")
else:
    print(f"Age {age}: Cannot vote")

# IMPLICIT CONVERSION (without bool())
print("\nIMPLICIT BOOLEAN CONVERSION")

# Numbers
count = 5
if count:  # Same as: if bool(count):
    print(f"Count {count} is non-zero")

zero = 0
if not zero:  # If it's false
    print(f"Zero is false")

# Strings
name = "John"
if name:
    print(f"Name: {name}")

password = ""
if not password:  # If it's false
    print("Password is empty")

# Lists
items = [1, 2, 3]
if items:
    print(f"You have {len(items)} items")

shopping_cart = []
if not shopping_cart:
    print("Cart is empty")

# SIMPLE EXAMPLES
print("\nSIMPLE EXAMPLES")

# Example: Check if item in stock
stock = 10
if stock > 0:
    print("Item in stock")
else:
    print("Out of stock")

# Example: Check user login
user = "alice"
if user:
    print(f"Welcome, {user}!")

# Example: Check grade
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(f"Score: {score}, Grade: {grade}")