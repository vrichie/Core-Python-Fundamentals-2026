# Python Strings Guide

This guide documents all string operations demonstrated in `Strings.py`, plus additional useful methods and operations for working with strings in Python.

---

## Table of Contents

1. [String Basics](#string-basics)
2. [Creating Strings](#creating-strings)
3. [Accessing String Characters](#accessing-string-characters)
4. [String Slicing](#string-slicing)
5. [String Methods](#string-methods)
6. [String Formatting](#string-formatting)
7. [String Operations](#string-operations)
8. [Escape Characters](#escape-characters)
9. [Built-in Functions](#built-in-functions)
10. [Complete Reference Table](#complete-reference-table)

---

## String Basics

A **string** is a sequence of characters enclosed in quotes. In Python, strings are:

- **Immutable**: Once created, you cannot change individual characters
- **Ordered**: Characters have a specific index position
- **Iterable**: You can loop through each character

```python
name = "Jerry"
print(type(name))  # <class 'str'>
```

---

## Creating Strings

### Single vs. Double Quotes

Both work identically; choose the one that keeps your code readable:

```python
print("Hello, this is a string")
print('single quotes still works')

# Use the opposite quote type inside
message = "She said 'hello'"
response = 'He said "goodbye"'
```

### Multi-line Strings (Triple Quotes)

Use triple quotes (`"""` or `'''`) for strings spanning multiple lines:

```python
bio = """I love computers
Python for me was easy to learn
it looks simple but powers alot of powerful tools
"""

print(bio)
# Output:
# I love computers
# Python for me was easy to learn
# it looks simple but powers alot of powerful tools
```

### Concatenation

Combine strings using the `+` operator:

```python
name = "Jerry"
middle = "Rig"

fullName = name + " " + middle
print(fullName)  # Jerry Rig
```

---

## Accessing String Characters

### Indexing (Single Character Access)

Strings use **0-based indexing**. Negative indices count from the end:

```python
name = "Jerry"

print(name[0])   # J (first character)
print(name[1])   # e
print(name[2])   # r
print(name[3])   # r
print(name[4])   # y (last character)
print(name[-1])  # y (last character)
print(name[-2])  # r (second-to-last)
```

### Iterating Through Characters

Loop through each character in a string:

```python
course = "Computer science"

for letter in course:
    print(letter)

# Output: C, o, m, p, u, t, e, r, (space), s, c, i, e, n, c, e
```

---

## String Slicing

**Slicing syntax:** `string[start:end:step]`

- `start`: Starting index (included)
- `end`: Ending index (NOT included)
- `step`: Increment (default: 1)

```python
course = "Computer science"

# Basic slicing
print(course[2:5])    # "mpu" (indices 2, 3, 4)

# From start to index 4
print(course[:5])     # "Compu"

# From index 2 to end
print(course[2:])     # "mputer science"

# Last 5 characters
print(course[-5:])    # "ence"

# Everything except last 2
print(course[:-2])    # "Computer scienc"

# From index -5 to -2
print(course[-5:-2])  # "enc"

# Every other character
print(course[::2])    # "Cmue cec"

# Reverse the string
print(course[::-1])   # "ecneics retupmoC"
```

**Quick slicing reference:**

| Slice | Result | Explanation |
|-------|--------|-------------|
| `s[2:5]` | chars at 2,3,4 | From index 2 to 4 |
| `s[:5]` | first 5 chars | From start to index 4 |
| `s[2:]` | from index 2 onward | From index 2 to end |
| `s[-5:]` | last 5 chars | From 5th from last to end |
| `s[:-2]` | all but last 2 | From start, excluding last 2 |
| `s[::2]` | every other char | Step of 2 |
| `s[::-1]` | reversed | Negative step of 1 |

---

## String Methods

Python strings have many built-in methods. Methods are functions called with dot notation: `string.method()`

### Case Conversion

```python
name = "Jerry"
welcome = "hello, world"

# uppercase()
print(name.upper())  # JERRY

# lowercase()
print(name.lower())  # jerry

# capitalize() - first char uppercase, rest lowercase
print(welcome.capitalize())  # Hello, world

# title() - capitalize first letter of each word
print(welcome.title())  # Hello, World

# swapcase() - swap upper and lower
print("HeLLo".swapcase())  # hEllO

# casefold() - aggressive lowercase (useful for comparisons)
print("ß".casefold())  # ss
```

### Searching & Checking

```python
text = "strawberry"

# in operator (check if substring exists)
print("berry" in text)   # True
print("apple" in text)   # False

# not in operator
print("apple" not in text)  # True

# startswith() - check if starts with substring
print(text.startswith("straw"))  # True
print(text.startswith("berry"))  # False

# endswith() - check if ends with substring
print(text.endswith("berry"))   # True
print(text.endswith("straw"))   # False

# find() - return index of first occurrence (returns -1 if not found)
print(text.find("b"))   # 5
print(text.find("z"))   # -1

# index() - like find() but raises error if not found
print(text.index("b"))  # 5
# print(text.index("z"))  # ValueError!

# count() - count occurrences
print(text.count("r"))  # 3
```

### String Replacement & Modification

```python
name = "Jerry"
fullName = "          Jerry Rig Everything    "

# replace() - replace all occurrences
print(name.replace('J', 'T'))  # Terry

# split() - split into list by delimiter
welcome = "hello, world"
print(welcome.split(','))  # ['hello', ' world']
print("a-b-c".split('-'))  # ['a', 'b', 'c']

# join() - opposite of split, combine list into string
words = ['hello', 'world']
print(' '.join(words))  # hello world
print('-'.join(['a', 'b', 'c']))  # a-b-c

# strip() - remove whitespace from both ends
print(fullName.strip())  # Jerry Rig Everything

# lstrip() - remove whitespace from left
print(fullName.lstrip())  # Jerry Rig Everything    (right spaces remain)

# rstrip() - remove whitespace from right
print(fullName.rstrip())  # (left spaces remain)Jerry Rig Everything

# strip with argument - remove specific characters
print("xxxHelloxxx".strip('x'))  # Hello
print("...python...".strip('.'))  # python
```

### Whitespace & Formatting

```python
text = "hello"
comment = "TRY AGAIN"

# center() - center text in field of given width
print(comment.casefold().center(20))  # "      try again     "

# ljust() - left justify
print(text.ljust(10))  # "hello     "

# rjust() - right justify
print(text.rjust(10))  # "     hello"

# zfill() - pad with zeros (useful for numbers)
print("42".zfill(5))  # "00042"

# expandtabs() - replace tabs with spaces
print("hello\tworld".expandtabs(4))  # "hello   world"
```

### Character Type Checking

These return `True` or `False`:

```python
# isalpha() - only letters
print("hello".isalpha())      # True
print("hello world".isalpha())  # False (space)
print("hello123".isalpha())   # False (numbers)

# isdigit() - only digits
print("12345".isdigit())      # True
print("123abc".isdigit())     # False

# isalnum() - letters or digits
print("hello123".isalnum())   # True
print("hello 123".isalnum())  # False (space)

# isspace() - only whitespace
print("   ".isspace())        # True
print(" \t".isspace())        # True (includes tabs, newlines)
print("a ".isspace())         # False

# isupper() - all letters uppercase
print("HELLO".isupper())      # True
print("Hello".isupper())      # False

# islower() - all letters lowercase
print("hello".islower())      # True
print("Hello".islower())      # False

# istitle() - title cased (first letter of each word upper)
print("Hello World".istitle())  # True
print("hello world".istitle())  # False

# isidentifier() - valid Python identifier
print("my_var".isidentifier()) # True
print("123var".isidentifier()) # False
print("my-var".isidentifier()) # False
```

### Other Useful Methods

```python
text = "strawberry"

# removeprefix() - remove prefix if present (Python 3.9+)
print("Hello World".removeprefix("Hello "))  # World

# removesuffix() - remove suffix if present (Python 3.9+)
print("Hello World".removesuffix(" World"))  # Hello

# partition() - split into 3 parts: (before, separator, after)
result = text.partition("r")
print(result)  # ('staw', 'r', 'berry')

# rpartition() - like partition but from right
result = text.rpartition("r")
print(result)  # ('strawbe', 'r', 'ry')

```

---

## String Formatting

### Escape Characters

Use backslash `\` to insert special characters:

```python
# \" - double quote
txt = "He said \"python is easy\", what do you think?"
print(txt)  # He said "python is easy", what do you think?

# \' - single quote
txt = 'He said \'hello\''
print(txt)  # He said 'hello'

# \n - newline
print("line1\nline2\nline3")
# Output:
# line1
# line2
# line3

# \t - tab
print("name\tage\tcity")  # name    age    city

# \\ - backslash
print("path\\to\\file")  # path\to\file

# \r - carriage return
print("hello\rworld")  # world (overwrites hello)
```

### f-Strings (Recommended - Python 3.6+)

The most modern and readable way to format strings:

```python
name = "Jerry"
age = 45
course = "Computer science"

# Basic interpolation
print(f"{name}")  # Jerry

# Expressions inside f-strings
print(f"{name} is {age} years old")  # Jerry is 45 years old

# Arithmetic
print(f"In 5 years, {name} will be {age + 5}")  # In 5 years, Jerry will be 50

# Formatting numbers (2 decimal places)
txt = f"{name} is {age:.2f}"
print(txt)  # Jerry is 45.00

# Right-aligned numbers with padding
price = 42.5
print(f"Price: ${price:>10.2f}")  # Price:      42.50

# Left-aligned
print(f"Name: {name:<20}")  # Name: Jerry              

# Center aligned
print(f"Course: {course:^30}")  #        Computer science       

# Percentage
percentage = 0.85
print(f"Score: {percentage:.1%}")  # Score: 85.0%
```

### String `.format()` Method (Older Style)

```python
name = "Jerry"
age = 45

# Positional arguments
print("Hello {} I am {}".format(name, age))  # Hello Jerry I am 45

# Named arguments
print("Hello {n} I am {a}".format(n=name, a=age))  # Hello Jerry I am 45

# Index positions
print("{0} {1} {0}".format("hello", "world"))  # hello world hello

# Format specifiers
price = 19.99
print("Price: ${:.2f}".format(price))  # Price: $19.99
```

### String Concatenation (Not Recommended)

```python
name = "Jerry"
age = 45

# String concatenation with +
print("Hello " + name + " I am " + str(age))  # Hello Jerry I am 45
# ❌ Slow and tedious for multiple variables
```

---

## String Operations

### Concatenation

```python
first = "Hello"
second = "World"

result = first + " " + second
print(result)  # Hello World
```

### Repetition

```python
print("abc" * 3)  # abcabcabc
print("* " * 5)   # * * * * * 
```

### Membership Testing

```python
text = "Python is awesome"

print("Python" in text)       # True
print("Java" in text)         # False
print("is" in text)           # True

if "Python" in text:
    print("Nerd, they love Python")
```

---

## Built-in Functions

### len() - Get String Length

```python
course = "Computer science"
print(len(course))  # 16 (including space)

name = "Jerry"
print(len(name))    # 5
```

### ord() - Get Unicode Code Point

```python
print(ord('A'))     # 65
print(ord('a'))     # 97
print(ord('1'))     # 49
```

### chr() - Convert Code Point to Character

```python
print(chr(65))      # A
print(chr(97))      # a
print(chr(49))      # 1
```

### max() & min() - Find Largest/Smallest Character

```python
name = "Jerry"
print(max(name))    # r (alphabetically highest)
print(min(name))    # J (alphabetically lowest)
```

### sorted() - Sort Characters

```python
word = "python"
print(sorted(word))  # ['h', 'o', 'n', 'p', 't', 'y']
print(''.join(sorted(word)))  # hnoptty
```

---

## Complete Reference Table

### String Methods Quick Reference

| Method | Purpose | Example | Result |
|--------|---------|---------|--------|
| `upper()` | Uppercase | `"hello".upper()` | `"HELLO"` |
| `lower()` | Lowercase | `"Hello".lower()` | `"hello"` |
| `capitalize()` | First letter upper | `"hello world".capitalize()` | `"Hello world"` |
| `title()` | Capitalize each word | `"hello world".title()` | `"Hello World"` |
| `swapcase()` | Swap case | `"HeLLo".swapcase()` | `"hEllO"` |
| `casefold()` | Aggressive lowercase | `"Straße".casefold()` | `"strasse"` |
| `find()` | Find substring index | `"hello".find("l")` | `2` |
| `index()` | Find substring index | `"hello".index("l")` | `2` |
| `count()` | Count occurrences | `"hello".count("l")` | `2` |
| `replace()` | Replace substring | `"hello".replace("l","L")` | `"heLLo"` |
| `split()` | Split into list | `"a,b,c".split(",")` | `["a","b","c"]` |
| `join()` | Join list into string | `",".join(["a","b"])` | `"a,b"` |
| `strip()` | Remove whitespace | `" hello ".strip()` | `"hello"` |
| `lstrip()` | Remove left whitespace | `" hello ".lstrip()` | `"hello "` |
| `rstrip()` | Remove right whitespace | `" hello ".rstrip()` | `" hello"` |
| `startswith()` | Check start | `"hello".startswith("he")` | `True` |
| `endswith()` | Check end | `"hello".endswith("lo")` | `True` |
| `center()` | Center in field | `"hi".center(6)` | `" hi   "` |
| `ljust()` | Left align | `"hi".ljust(6)` | `"hi    "` |
| `rjust()` | Right align | `"hi".rjust(6)` | `"    hi"` |
| `zfill()` | Pad with zeros | `"42".zfill(4)` | `"0042"` |
| `isalpha()` | All letters? | `"hello".isalpha()` | `True` |
| `isdigit()` | All digits? | `"123".isdigit()` | `True` |
| `isalnum()` | Letters/digits? | `"hello123".isalnum()` | `True` |
| `isspace()` | All whitespace? | `"  ".isspace()` | `True` |
| `isupper()` | All uppercase? | `"HELLO".isupper()` | `True` |
| `islower()` | All lowercase? | `"hello".islower()` | `True` |
| `istitle()` | Title cased? | `"Hello World".istitle()` | `True` |

---

## Common Patterns & Examples

### Check if String Contains Specific Word

```python
text = "Python is awesome"

# Check for exact word (might match part of word)
if "Python" in text:
    print("Found!")  # ✓ Works

# Better: check for word boundaries (needs regex for real use)
words = text.split()
if "is" in words:
    print("Found the word 'is'")  # ✓ Works
```

### Parse Comma-Separated Values

```python
csv_line = "John,30,Engineer"
fields = csv_line.split(',')
print(fields)  # ['John', '30', 'Engineer']
```

### Create Formatted Output

```python
items = ["apple", "banana", "cherry"]
formatted = ", ".join(items)
print(f"Items: {formatted}")  # Items: apple, banana, cherry
```

### Validate User Input

```python
password = input("Enter password: ")

if len(password) < 8:
    print("Too short!")
elif not any(c.isupper() for c in password):
    print("Need uppercase!")
elif not any(c.isdigit() for c in password):
    print("Need a number!")
else:
    print("Strong password!")
```

### Remove Specific Characters

```python
phone = "123-456-7890"
digits_only = phone.replace("-", "")
print(digits_only)  # 1234567890
```

### Reverse a String

```python
word = "python"
reversed_word = word[::-1]
print(reversed_word)  # nohtyp
```

### Clean Whitespace

```python
messy = "  hello   world  \n"
clean = messy.strip()
print(f"'{clean}'")  # 'hello   world'
```

---

## Running the Examples

```bash
python3 Strings.py
```

All examples from `Strings.py` will run with various text outputs demonstrating string operations.

---

## Tips & Best Practices

1. **Use f-strings** (Python 3.6+) for modern string formatting
2. **Use `in` operator** to check if substring exists (fast and readable)
3. **Remember strings are immutable** — methods return new strings, they don't modify the original
4. **Use `strip()` on user input** to remove accidental whitespace
5. **Use `.split()` and `.join()`** to work with lists of strings
6. **Check string type** with methods like `.isdigit()`, `.isalpha()` before processing
7. **Use triple quotes** for multi-line strings
8. **Escape special characters** only when needed in strings
