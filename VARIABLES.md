# Python Variables & Data Types Guide

This guide explains the concepts demonstrated in `variables.py`, including variable naming conventions, Python's built-in data types, and when to use each collection type.

---

## Table of Contents

1. [Python Data Types Overview](#python-data-types-overview)
2. [Variable Naming Conventions](#variable-naming-conventions)
3. [Basic Data Types](#basic-data-types)
4. [Type Casting](#type-casting)
5. [Multiple Value Assignment](#multiple-value-assignment)
6. [Collection Types Deep Dive](#collection-types-deep-dive)
7. [Quick Reference: Choosing the Right Collection](#quick-reference-choosing-the-right-collection)

---

## Python Data Types Overview

Python has the following main data type categories:

| Category | Types | Example |
|----------|-------|---------|
| **Text Type** | `str` | `"Hello"` |
| **Numeric Types** | `int`, `float`, `complex` | `5`, `3.14`, `2+3j` |
| **Sequence Types** | `list`, `tuple`, `range` | `[1, 2, 3]`, `(1, 2, 3)` |
| **Mapping Type** | `dict` | `{"name": "James"}` |
| **Set Types** | `set`, `frozenset` | `{1, 2, 3}` |
| **Boolean Type** | `bool` | `True`, `False` |
| **Binary Types** | `bytes`, `bytearray`, `memoryview` | `b'hello'` |
| **None Type** | `NoneType` | `None` |

---

## Variable Naming Conventions

### Valid Variable Names

Variable names in Python can contain letters, digits, and underscores. They must start with a letter or underscore (not a digit).

```python
myvar = "test"          # lowercase
my_var = "test"         # with underscore
_my_var = "test"        # starting with underscore (convention: private)
```

### Naming Styles

Python supports three popular naming conventions:

#### 1) **camelCase** (used in other languages, not recommended for Python)

```python
varName = "camel case"  # first word lowercase, subsequent words capitalized
```

When to use: Less common in Python; more used in JavaScript, Java, etc.

#### 2) **PascalCase** (used for class names)

```python
class VarName:          # each word capitalized
    pass
```

When to use: **Always use for class definitions** (Python convention).

#### 3) **snake_case** (recommended for Python variables and functions)

```python
var_name = "snake case"  # words separated by underscores, all lowercase
```

When to use: **Best practice for regular variables and function names** in Python ([PEP 8](https://pep8.org/)).

---

## Basic Data Types

### 1. Numbers

#### Integers (`int`)

```python
num1 = 1
print(type(num1))  # <class 'int'>
```

- Whole numbers without decimal points
- Can be positive, negative, or zero
- No size limit in Python

#### Floats (`float`)

```python
num2 = 2.3
print(type(num2))  # <class 'float'>
```

- Numbers with decimal points
- Used for calculations requiring precision
- Can also represent numbers in scientific notation: `1.5e-3` (0.0015)

#### Complex Numbers (`complex`)

```python
num_complex = 2 + 3j
print(type(num_complex))  # <class 'complex'>
print(num_complex.real)   # 2.0
print(num_complex.imag)   # 3.0
```

- Represent numbers with real and imaginary parts
- Used in advanced mathematics and engineering

### 2. Strings (`str`)

Strings are text enclosed in quotes (single or double quotes are equivalent):

```python
name = "James"      # double quotes
grade = 'A'         # single quotes

print(name)         # James
print(grade)        # A
```

**Multi-line strings:**

```python
message = """This is a
multi-line
string"""
```

### 3. Booleans (`bool`)

```python
is_active = True
is_deleted = False
```

- Only two values: `True` or `False`
- Used in conditional logic
- Everything in Python has a "truthiness": empty collections, 0, None, empty strings are "falsy"; everything else is "truthy"

---

## Type Casting

Type casting means converting one data type to another. Python provides built-in functions for this:

```python
# Converting float to string
num2 = 2.3
num3_as_string = str(num2)
print(type(num3_as_string))  # <class 'str'>
print(num3_as_string)        # "2.3"

# String concatenation with casted value
grade = 'A'
result = num3_as_string + grade
print(result)  # "2.3A"
```

### Common Casting Functions

```python
# To string
str(123)           # "123"
str(45.67)         # "45.67"

# To integer
int("123")         # 123
int(45.67)         # 45 (truncates decimal)
int("0101", 2)     # 5 (binary to decimal)

# To float
float("3.14")      # 3.14
float(5)           # 5.0

# To boolean
bool(1)            # True
bool(0)            # False
bool("")           # False (empty string)
bool("hello")      # True (non-empty string)
```

---

## Multiple Value Assignment

Python allows assigning multiple values to multiple variables in a single line:

```python
a, b, c = 23, "hake", 89.9

print(a)  # 23
print(b)  # hake
print(c)  # 89.9
```

The number of variables and values must match:

```python
# ✓ Valid
x, y = 1, 2

# ✗ Error: too many values to unpack
x, y = 1, 2, 3

# ✓ Valid with unpacking
x, *y = 1, 2, 3, 4  # x=1, y=[2, 3, 4]
```

---

## Collection Types Deep Dive

Collections allow you to store multiple items in a single variable. Python has four main collection types, each with different characteristics.

### 1. **Lists** (`list`)

A **list** is an ordered, mutable (changeable) collection that allows duplicate items.

```python
# Creating a list
fruits = ['apple', 'banana', 'cherry']
mixed = ['Hello', 'world', 'test', 12]

print(mixed)  # ['Hello', 'world', 'test', 12]
print(type(mixed))  # <class 'list'>
```

#### List Operations

```python
# Access by index (0-based)
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])    # apple
print(fruits[-1])   # cherry (last item)

# Slicing
print(fruits[0:2])  # ['apple', 'banana']

# Modifying
fruits[0] = 'orange'  # Replace
fruits.append('date')  # Add to end
fruits.insert(1, 'kiwi')  # Insert at position
fruits.remove('banana')  # Remove specific item
popped = fruits.pop()  # Remove and return last item

# Length
print(len(fruits))  # number of items

# Check membership
if 'apple' in fruits:
    print("Found!")

# Iterate
for fruit in fruits:
    print(fruit)

# Sort
numbers = [3, 1, 2]
numbers.sort()  # [1, 2, 3]
```

#### When to Use Lists

- ✓ When you need an **ordered** collection
- ✓ When you need to **add, remove, or modify** items
- ✓ When **duplicates are allowed**
- ✓ Accessing items by **index** matters

**Example Use Case:**
```python
# Shopping list (order matters, may have duplicates)
shopping_list = ['milk', 'eggs', 'bread', 'milk']
shopping_list.append('butter')
```

---

### 2. **Tuples** (`tuple`)

A **tuple** is an ordered, immutable (unchangeable) collection that allows duplicate items.

```python
# Creating a tuple
coordinates = ('a', 'a', 'f', 'h')
point = (10, 20)

print(coordinates)  # ('a', 'a', 'f', 'h')
print(type(coordinates))  # <class 'tuple'>
```

#### Tuple Operations

```python
coordinates = (10, 20, 30)

# Access by index (like lists)
print(coordinates[0])    # 10
print(coordinates[-1])   # 30

# Slicing (like lists)
print(coordinates[0:2])  # (10, 20)

# Length
print(len(coordinates))  # 3

# Check membership
if 10 in coordinates:
    print("Found!")

# Iterate
for coord in coordinates:
    print(coord)

# Count occurrences
duplicates = ('a', 'b', 'a', 'c', 'a')
print(duplicates.count('a'))  # 3
```

#### What You CANNOT do with Tuples

```python
coordinates = (10, 20, 30)

# ✗ Cannot modify
coordinates[0] = 5  # TypeError!

# ✗ Cannot append
coordinates.append(40)  # AttributeError!

# ✗ Cannot delete individual item
del coordinates[0]  # TypeError!
```

#### When to Use Tuples

- ✓ When you need **constant/immutable data**
- ✓ When you want to **prevent accidental changes**
- ✓ When you need to use it as a **dictionary key** (lists cannot be keys)
- ✓ When you want **better performance** (tuples are slightly faster)
- ✓ When returning **multiple values from a function**

**Example Use Cases:**
```python
# Function returning multiple values
def get_user():
    return ("James", 48, "james@email.com")

name, age, email = get_user()

# Dictionary keys (tuples work, lists don't)
locations = {
    (40.7128, 74.0060): "New York",  # ✓ tuple as key
    (51.5074, 0.1278): "London"
}

# Coordinate-like data
rgb_color = (255, 128, 0)  # Red-Green-Blue values
```

---

### 3. **Sets** (`set`)

A **set** is an unordered, mutable collection with NO duplicates and NO indexing.

```python
# Creating a set
colors = {"red", "orange", "black"}

print(colors)  # {'red', 'orange', 'black'} (order not guaranteed)
print(type(colors))  # <class 'set'>
```

**Important:** Set order is not guaranteed! Items may print in different order.

#### Set Operations

```python
colors = {"red", "green", "blue"}

# Add items
colors.add("yellow")

# Remove items
colors.remove("red")        # Raises error if not found
colors.discard("yellow")    # No error if not found

# Check membership (fast!)
if "blue" in colors:
    print("Found!")

# Length
print(len(colors))  # 3

# Iterate (order not guaranteed)
for color in colors:
    print(color)

# Set operations (mathematical)
set1 = {1, 2, 3}
set2 = {2, 3, 4}

union = set1 | set2          # {1, 2, 3, 4} (combine)
intersection = set1 & set2   # {2, 3} (common)
difference = set1 - set2     # {1} (in set1 but not set2)
symmetric_diff = set1 ^ set2 # {1, 4} (in either but not both)
```

#### What You CANNOT do with Sets

```python
colors = {"red", "green", "blue"}

# ✗ Cannot access by index
print(colors[0])  # TypeError!

# ✗ Cannot have duplicates
colors = {"red", "red", "blue"}  # Really {'red', 'blue'}
```

#### When to Use Sets

- ✓ When you need to **remove duplicates**
- ✓ When **order doesn't matter**
- ✓ When you need **fast membership checking**
- ✓ When you need **mathematical set operations** (union, intersection, etc.)
- ✓ When you **don't need indexing**

**Example Use Cases:**
```python
# Remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)  # {1, 2, 3, 4}

# Find common tags between users
user1_tags = {"python", "coding", "data"}
user2_tags = {"python", "web", "javascript"}
common = user1_tags & user2_tags  # {"python"}

# Check if user has permission (fast lookup)
admin_users = {"alice", "bob", "charlie"}
if username in admin_users:  # Very fast!
    grant_access()
```

---

### 4. **Dictionaries** (`dict`)

A **dictionary** is an unordered, mutable collection of key-value pairs. Keys must be unique.

```python
# Creating a dictionary
person = {"name": "James", "age": 48}

print(person)  # {'name': 'James', 'age': 48}
print(type(person))  # <class 'dict'>
```

#### Dictionary Operations

```python
person = {"name": "James", "age": 48, "grade": "A"}

# Access by key (not index!)
print(person["name"])     # James
print(person.get("age"))  # 48
print(person.get("email", "N/A"))  # N/A (default if not found)

# Modify
person["age"] = 49        # Update
person["email"] = "james@email.com"  # Add new key

# Delete
del person["grade"]
person.pop("email")

# Check if key exists
if "name" in person:
    print("Name exists!")

# Get all keys, values, items
print(person.keys())       # dict_keys(['name', 'age'])
print(person.values())     # dict_values(['James', 49])
print(person.items())      # dict_items([('name', 'James'), ('age', 49)])

# Iterate
for key, value in person.items():
    print(f"{key}: {value}")

for key in person:
    print(key)

# Length
print(len(person))  # 2

# Merge dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}  # {"a": 1, "b": 2, "c": 3, "d": 4}
```

#### When to Use Dictionaries

- ✓ When data has **clear relationships** (key-value pairs)
- ✓ When you need to **access by meaningful key** (not index)
- ✓ When you need **fast lookup** by key
- ✓ When you need **structured data** (like JSON, database rows)
- ✓ When working with **configuration**, **mappings**, or **lookups**

**Example Use Cases:**
```python
# User profile
user = {
    "id": 1,
    "name": "James",
    "age": 48,
    "email": "james@email.com",
    "tags": ["python", "coding"]
}

# Configuration settings
config = {
    "debug": True,
    "port": 8000,
    "database": "postgresql",
    "timeout": 30
}

# Lookup table (translate grades)
grade_map = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0
}
score = grade_map["A"]  # 90

# Frequency counter
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
# {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

---

## Quick Reference: Choosing the Right Collection

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| **Ordered** | ✓ Yes | ✓ Yes | ✗ No | ✗ No* |
| **Mutable** | ✓ Yes | ✗ No | ✓ Yes | ✓ Yes |
| **Allows Duplicates** | ✓ Yes | ✓ Yes | ✗ No | ✗ No (keys) |
| **Indexed/Keyed** | ✓ Index | ✓ Index | ✗ No | ✓ Key |
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` | `{"a": 1}` |
| **Speed** | Medium | Fast | Very Fast | Very Fast |

*Dict order is preserved in Python 3.7+

### Decision Tree

```
Do you need key-value pairs?
├─ YES → Use DICT
└─ NO → Continue...
    
Do you need to modify the collection?
├─ NO → Use TUPLE (immutable, faster)
└─ YES → Continue...
    
Do you need duplicates OR order to matter?
├─ YES → Use LIST (ordered, allows duplicates)
└─ NO → Use SET (no duplicates, fast lookup)
```

---

## Complete Example from `variables.py`

```python
# Basic types
num1 = 1
num2 = 2.3
name = "James"
grade = 'A'

# Type casting
num3_as_string = str(num2)
result = num3_as_string + grade  # "2.3A"

# Multiple assignment
a, b, c = 23, "hake", 89.9

# Collections
dt_list = ['Hello', 'world', 'test', 12]      # List
dt_tuple = ('a', 'a', 'f', 'h')               # Tuple
dt_dict = {"name": "James", "age": 48}        # Dict
dt_set = {"red", "orange", "black"}           # Set
dt_bool = True                                # Boolean

print(type(dt_list))    # <class 'list'>
print(type(dt_tuple))   # <class 'tuple'>
print(type(dt_dict))    # <class 'dict'>
print(type(dt_set))     # <class 'set'>
print(type(dt_bool))    # <class 'bool'>
```

---

## Tips & Best Practices

1. **Use snake_case** for variable names (Python convention)
2. **Use meaningful variable names**: `user_age` is better than `ua`
3. **Type cast explicitly** when mixing types: `str(num) + text` instead of relying on automatic conversion
4. **Choose the right collection**:
   - Need order and modification? → **List**
   - Need immutable data? → **Tuple**
   - Need unique items or set operations? → **Set**
   - Need key-value lookups? → **Dict**
5. **Use f-strings** for cleaner formatting: `f"{name} is {age}"` instead of `name + " is " + str(age)`

---

## Running the Examples

```bash
python3 variables.py
```

Try modifying `variables.py` to experiment with:
- Different data types
- Type casting
- List/tuple/set/dict operations
- Variable naming conventions
