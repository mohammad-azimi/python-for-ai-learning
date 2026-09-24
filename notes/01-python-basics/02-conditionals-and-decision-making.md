# Conditionals and Decision Making — Lesson 02

## Overview

In this lesson, I learned how Python programs can make decisions based on conditions.

The main concepts are:

- Boolean conditions
- Comparison operators
- `if`
- `elif`
- `else`
- Indentation
- `and`
- `or`
- `not`
- String comparison
- Nested conditions
- Simple rule-based decision systems

---

# 1. The `if` Statement

The `if` statement executes code only when a condition is true.

```python
stress_score = 8

if stress_score > 7:
    print("High stress")
```

Output:

```text
High stress
```

The expression:

```python
stress_score > 7
```

produces either:

```python
True
```

or:

```python
False
```

---

# 2. Boolean Conditions

Conditions in Python eventually evaluate to a Boolean value.

```python
print(8 > 7)
```

Output:

```text
True
```

Another example:

```python
print(3 > 7)
```

Output:

```text
False
```

---

# 3. Comparison Operators

## Greater Than

```python
>
```

Example:

```python
print(10 > 5)
```

---

## Less Than

```python
<
```

Example:

```python
print(3 < 8)
```

---

## Greater Than or Equal To

```python
>=
```

Example:

```python
print(7 >= 7)
```

---

## Less Than or Equal To

```python
<=
```

Example:

```python
print(5 <= 7)
```

---

## Equal To

```python
==
```

Example:

```python
age = 25

print(age == 25)
```

---

## Not Equal To

```python
!=
```

Example:

```python
age = 25

print(age != 18)
```

---

# 4. Difference Between `=` and `==`

This is an important distinction.

```python
age = 25
```

means:

Assign the value `25` to the variable `age`.

But:

```python
age == 25
```

means:

Check whether the value of `age` is equal to `25`.

Therefore:

```text
=   Assignment
==  Comparison
```

---

# 5. Indentation

Python uses indentation to determine which statements belong to a condition.

Correct:

```python
temperature = 38

if temperature > 37:
    print("High temperature")
```

The indented line belongs to the `if` statement.

Python usually uses four spaces for indentation.

---

# 6. The `else` Statement

`else` is executed when the `if` condition is false.

```python
stress_score = 5

if stress_score > 7:
    print("High stress")
else:
    print("Stress is not high")
```

Output:

```text
Stress is not high
```

---

# 7. The `elif` Statement

`elif` allows a program to check multiple conditions.

Example:

```python
stress_score = 6

if stress_score >= 8:
    print("High stress")
elif stress_score >= 4:
    print("Moderate stress")
else:
    print("Low stress")
```

Output:

```text
Moderate stress
```

Python checks these conditions from top to bottom.

Once one condition is true, the remaining `elif` and `else` branches are skipped.

---

# 8. Order of Conditions

The order of conditions matters.

Incorrect logical order:

```python
stress_score = 9

if stress_score >= 4:
    print("Moderate stress")
elif stress_score >= 8:
    print("High stress")
```

The first condition is already true for `9`, so Python prints:

```text
Moderate stress
```

A better order is:

```python
if stress_score >= 8:
    print("High stress")
elif stress_score >= 4:
    print("Moderate stress")
else:
    print("Low stress")
```

More restrictive conditions should usually be checked first.

---

# 9. The `and` Operator

`and` requires all connected conditions to be true.

```python
stress_score = 8
sleep_hours = 5

if stress_score >= 7 and sleep_hours < 6:
    print("High risk")
```

Both conditions are true:

```text
8 >= 7
5 < 6
```

Therefore:

```text
True and True → True
```

Truth table:

```text
True  and True  → True
True  and False → False
False and True  → False
False and False → False
```

---

# 10. The `or` Operator

`or` requires at least one condition to be true.

```python
stress_score = 9
sleep_hours = 8

if stress_score >= 8 or sleep_hours < 5:
    print("Attention needed")
```

The first condition is true even though the second condition is false.

```text
True or False → True
```

---

# 11. Difference Between `and` and `or`

`and` means that all required conditions must be true.

`or` means that at least one condition must be true.

Example:

```python
high_stress = True
low_sleep = False
```

This condition is false:

```python
high_stress and low_sleep
```

But this condition is true:

```python
high_stress or low_sleep
```

---

# 12. The `not` Operator

`not` reverses a Boolean value.

```python
is_sleeping = False

print(not is_sleeping)
```

Output:

```text
True
```

Because:

```text
not False → True
not True  → False
```

---

# 13. Combining Conditions

Conditions can be combined to create more useful decision rules.

```python
heart_rate = 95
sleep_hours = 5
stress_score = 8

if stress_score >= 8 and sleep_hours < 6:
    print("High stress risk")
elif stress_score >= 5:
    print("Moderate stress risk")
else:
    print("Low stress risk")
```

---

# 14. Conditions with User Input

Conditions can work with values entered by the user.

```python
stress_score = float(
    input("Enter your stress score: ")
)

if stress_score >= 8:
    print("High stress")
elif stress_score >= 4:
    print("Moderate stress")
else:
    print("Low stress")
```

---

# 15. Conditions with Strings

Conditions can also compare strings.

```python
status = "awake"

if status == "awake":
    print("The person is awake")
```

Python strings are case-sensitive.

Therefore:

```python
"Awake" == "awake"
```

produces:

```text
False
```

---

# 16. Nested Conditions

A condition can be placed inside another condition.

```python
stress_score = 8
sleep_hours = 5

if stress_score >= 7:
    print("Stress is high")

    if sleep_hours < 6:
        print("Sleep is also low")
```

This is called a nested condition.

When possible, some nested conditions can be simplified using logical operators.

For example:

```python
if stress_score >= 7 and sleep_hours < 6:
    print("High stress and low sleep")
```

---

# 17. Simple Rule-Based Decision System

A small decision system can combine multiple inputs:

```python
heart_rate = float(input("Enter heart rate: "))
sleep_hours = float(input("Enter sleep hours: "))
stress_score = float(input("Enter stress score: "))

if stress_score >= 8 and sleep_hours < 6:
    print("Risk level: High")
elif stress_score >= 5 or heart_rate > 90:
    print("Risk level: Moderate")
else:
    print("Risk level: Low")
```

The program uses several features to determine a result.

---

# 18. Rule-Based Systems vs Machine Learning

The previous program is a rule-based system.

For example:

```python
if stress_score >= 8:
```

The threshold `8` was selected manually.

The program does not learn this rule automatically.

In a rule-based system:

```text
Human → defines the rules
```

In Machine Learning:

```text
Data → model learns patterns
```

A Machine Learning model might receive features such as:

```text
heart_rate
sleep_hours
stress_score
activity_level
temperature
EEG features
```

and learn patterns from previous examples.

Understanding conditions helps build a foundation for understanding decision logic before moving to Machine Learning models.

---

# Key Points

`if` checks a condition.

`elif` checks another condition when previous conditions are false.

`else` handles the remaining case.

Comparison operators include:

```text
>
<
>=
<=
==
!=
```

Logical operators include:

```text
and
or
not
```

Python checks an `if / elif / else` structure from top to bottom.

Indentation is part of Python syntax.

Conditions can work with numbers, strings, Boolean values, and user input.

Rule-based systems use rules written by humans, while Machine Learning models learn patterns from data.
