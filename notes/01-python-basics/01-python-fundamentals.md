# Python Fundamentals — Lesson 01

## Overview

In this lesson, I learned the first fundamental concepts of Python with a focus on building a foundation for Artificial Intelligence and Machine Learning.

Topics covered:

- `print()`
- Variables
- Basic data types
- `type()`
- Arithmetic operations
- `input()`
- Type conversion
- Simple average calculation

---

# 1. The `print()` Function

The `print()` function is used to display information on the screen.

```python
print("Hello")
```

Output:

```text
Hello
```

Another example:

```python
print("I am learning Python")
```

---

# 2. Variables

A variable can be thought of as a named container that stores a value.

Example:

```python
age = 25
```

Here:

```text
Variable name: age
Value: 25
```

We can display the value using `print()`:

```python
age = 25

print(age)
```

Output:

```text
25
```

## AI-Related Example

Variables can represent information from a dataset.

```python
heart_rate = 82
stress_level = 7
sleep_hours = 6

print(heart_rate)
print(stress_level)
print(sleep_hours)
```

Later, Machine Learning datasets may contain thousands or millions of values like these.

---

# 3. Basic Data Types

Four important Python data types were introduced.

## Integer — `int`

An integer represents a whole number.

```python
age = 25
```

Examples:

```python
10
25
-5
1000
```

---

## Floating-Point Number — `float`

A float represents a decimal number.

```python
temperature = 36.7
```

Example related to Artificial Intelligence:

```python
weight = 0.847
```

Floating-point numbers are very common in Machine Learning because model weights, probabilities, measurements, and many other values are decimal numbers.

---

## String — `str`

A string represents text.

```python
name = "Mohammad"
```

Another example:

```python
field = "Artificial Intelligence"
```

---

## Boolean — `bool`

A Boolean represents one of two values:

```python
True
False
```

Example:

```python
is_stressed = True
```

or:

```python
is_stressed = False
```

---

# 4. Checking the Type of a Variable

The `type()` function shows the data type of a value.

Example:

```python
age = 25

print(type(age))
```

Output:

```text
<class 'int'>
```

More examples:

```python
temperature = 36.7
name = "Mohammad"
is_stressed = True

print(type(temperature))
print(type(name))
print(type(is_stressed))
```

---

# 5. Arithmetic Operations

Python can perform mathematical operations.

```python
a = 10
b = 3
```

## Addition

```python
print(a + b)
```

## Subtraction

```python
print(a - b)
```

## Multiplication

```python
print(a * b)
```

## Division

```python
print(a / b)
```

## Exponentiation

```python
print(a ** b)
```

For example:

```python
print(2 ** 3)
```

Output:

```text
8
```

Because:

```text
2 × 2 × 2 = 8
```

---

# 6. Simple Data Analysis Example

Suppose the number of sleep hours for three days is:

```python
day1 = 6
day2 = 7
day3 = 5
```

The average can be calculated as:

```python
average_sleep = (day1 + day2 + day3) / 3

print(average_sleep)
```

Output:

```text
6.0
```

This is a simple example of calculating an average from data.

Later, libraries such as NumPy and Pandas can perform similar calculations on much larger datasets.

---

# 7. User Input

The `input()` function allows a program to receive information from the user.

Example:

```python
name = input("Enter your name: ")

print(name)
```

If the user enters:

```text
Mohammad
```

the value is stored in the variable `name`.

---

# 8. Type Conversion

Values received using `input()` are strings by default.

For example:

```python
age = input("Enter your age: ")
```

Even if the user enters:

```text
25
```

Python receives it as text.

To convert the value to an integer:

```python
age = int(input("Enter your age: "))
```

For decimal numbers:

```python
weight = float(input("Enter your weight: "))
```

---

# Key Points

- `print()` displays information.
- Variables store values.
- `int` represents whole numbers.
- `float` represents decimal numbers.
- `str` represents text.
- `bool` represents `True` or `False`.
- `type()` shows the data type of a value.
- Python can perform mathematical operations.
- `input()` receives information from the user.
- `int()` and `float()` can convert input values into numbers.
- Simple calculations such as averages are basic examples of working with data.
