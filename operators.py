# ARITHMETIC OPERATORS
# +, -, *, /, %, **, //

print("\nARITHMETIC OPERATORS")
a = 50
b = 4

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")

# Check even or odd
print(f"\n17 is even: {17 % 2 == 0}")
print(f"17 is odd: {17 % 2 != 0}")

# ASSIGNMENT OPERATORS
# =, +=, -=, *=, /=, etc.

print("\nASSIGNMENT OPERATORS")
x = 10
print(f"x = {x}")

x += 5
print(f"x += 5 → x = {x}")

x -= 3
print(f"x -= 3 → x = {x}")

x *= 2
print(f"x *= 2 → x = {x}")

# Shopping example
print("\nCounting total items:")
total = 0
total += 5   # Add 5 items
total += 3   # Add 3 more items
print(f"Total items: {total}")

# COMPARISON OPERATORS
# ==, !=, >, <, >=, <=

print("\nCOMPARISON OPERATORS")
a = 50
b = 4

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

# Real-world example
print("\nAge check:")
age = 25
if age >= 18:
    print(f"Age {age}: Can vote")
else:
    print(f"Age {age}: Cannot vote")

print("\nGrade assignment:")
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(f"Score {score}: Grade {grade}")