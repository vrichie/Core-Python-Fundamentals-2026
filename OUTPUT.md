# Output Examples (Python)

This small folder demonstrates basic `print()` usage, string formatting, and simple variables. The main example is in `output.py` and produces a text banner plus a greeting that mixes strings and numbers.

## Files

- `output.py`: Prints a banner and a greeting that combines text with variables.
- `variables.py`: Empty placeholder for future variable examples.

## What `output.py` does

### 1) Prints a text banner

The script builds three string lines and prints them in order to form a box with the word "WELCOME" centered.

```python
line1 = "*******************"
line2 = "*                 *"
line3 = "*     WELCOME     *"

print(line1)
print(line2)
print(line3)
print(line2)
print(line1)
```

Expected output:

```
*******************
*                 *
*     WELCOME     *
*                 *
*******************
```

### 2) Prints a greeting with variables

The script defines a name and age, then prints a sentence. Notice it uses `+` for string concatenation and `,` to print a number without converting it to a string first.

```python
name = "James"
age = 20

print("Hello my name is "+name+" i am ", age, " years old")
```

Expected output:

```
Hello my name is James i am  20  years old
```

Note: the extra spaces come from how `print()` inserts spaces between comma-separated values.

## Run the example

From this folder:

```bash
python3 output.py
```

## Additional examples you can try

These are small variations you can copy into `output.py` (or place in `variables.py`) to see different `print()` behaviors.

### A) Use f-strings for cleaner formatting

```python
name = "James"
age = 20
print(f"Hello my name is {name} and I am {age} years old")
```

Expected output:

```
Hello my name is James and I am 20 years old
```

### B) Control the end-of-line with `end=`

```python
print("Hello", end=" ")
print("world")
```

Expected output:

```
Hello world
```

### C) Repeat characters with `*`

```python
print("*" * 10)
print("-" * 10)
```

Expected output:

```
**********
----------
```

### D) Build the banner dynamically

```python
title = "WELCOME"
width = len(title) + 6
border = "*" * width
middle = f"*  {title}  *"
empty = "*" + " " * (width - 2) + "*"

print(border)
print(empty)
print(middle)
print(empty)
print(border)
```

Expected output:

```
************
*          *
*  WELCOME *
*          *
************
```

## Notes

- If you want to avoid the extra spaces in the greeting, either convert the number to a string with `str(age)` or use f-strings.
- `variables.py` is empty right now and is a good place to add your own experiments.
