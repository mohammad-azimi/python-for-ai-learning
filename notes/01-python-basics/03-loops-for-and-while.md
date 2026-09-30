# Loops — `for` and `while` — Lesson 03

## Overview

In this lesson, I learned how Python can repeat operations.

Loops are especially useful when working with multiple values, such as samples in a dataset.

Topics covered:

- `for` loops
- Iteration
- Loop variables
- Loops over simple lists
- Combining `for` with `if`
- `range()`
- `range(start, stop, step)`
- Counters
- Accumulation
- `+=`
- Calculating averages with loops
- Counting values that satisfy a condition
- `while` loops
- Infinite loops
- Choosing between `for` and `while`
- Simple data-processing examples

---

# 1. Why Do We Need Loops?

Suppose we want to print several values:

```python
print(3)
print(5)
print(8)
print(2)
print(7)
```

This works for a few values, but it becomes impractical when we have hundreds or thousands of values.

A loop allows us to repeat an operation automatically.

---

# 2. The `for` Loop

A basic `for` loop:

```python
for number in [1, 2, 3, 4, 5]:
    print(number)
```

Output:

```text
1
2
3
4
5
```

Python takes each value one at a time and stores it temporarily in `number`.

---

# 3. Iteration

Each execution of the loop is called an iteration.

Example:

```python
for number in [1, 2, 3]:
    print(number)
```

There are three iterations:

```text
Iteration 1 → number = 1
Iteration 2 → number = 2
Iteration 3 → number = 3
```

---

# 4. Loop Variable Names

The loop variable can have any valid name.

```python
for x in [1, 2, 3]:
    print(x)
```

A meaningful name is usually better:

```python
for stress in [2, 5, 8]:
    print(stress)
```

---

# 5. Looping Over Data

Example with stress values:

```python
stress_levels = [3, 8, 5, 9, 2]

for stress in stress_levels:
    print(stress)
```

Python processes the values one by one.

This is a basic example of processing multiple data samples.

---

# 6. Combining `for` and `if`

A loop can contain a condition:

```python
stress_levels = [3, 8, 5, 9, 2]

for stress in stress_levels:
    if stress >= 7:
        print("High stress")
    else:
        print("Normal stress")
```

A separate decision is made for every value.

---

# 7. Indentation in Loops

Indentation determines which code belongs to the loop.

Correct:

```python
for number in [1, 2, 3]:
    print(number)
```

The indented line is executed during every iteration.

---

# 8. Multiple Conditions Inside a Loop

We can use `if`, `elif`, and `else` inside a loop.

```python
stress_levels = [3, 8, 5, 9]

for stress in stress_levels:
    if stress >= 8:
        print("High")
    elif stress >= 5:
        print("Moderate")
    else:
        print("Low")
```

This allows each data sample to be classified independently.

---

# 9. The `range()` Function

`range()` is commonly used with loops.

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

`range(5)` starts from `0` and stops before `5`.

---

# 10. Starting From Zero

Python commonly uses zero-based indexing.

For example:

```python
values = [10, 20, 30]
```

The first value is later accessed using:

```python
values[0]
```

which gives:

```text
10
```

---

# 11. `range()` With Start and Stop

Example:

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

The start value is included.

The stop value is excluded.

---

# 12. `range()` With Step

The third argument defines the step:

```python
for number in range(0, 10, 2):
    print(number)
```

Output:

```text
0
2
4
6
8
```

General form:

```python
range(start, stop, step)
```

---

# 13. Using a Counter

A common loop variable is `i`.

```python
for i in range(5):
    print("Iteration:", i)
```

Output:

```text
Iteration: 0
Iteration: 1
Iteration: 2
Iteration: 3
Iteration: 4
```

---

# 14. Connection to AI Training

Loops are used repeatedly in Machine Learning and Deep Learning.

A simple conceptual example:

```python
for epoch in range(5):
    print("Training epoch:", epoch)
```

A training process may conceptually look like:

```python
for epoch in range(100):
    train_model()
```

This means repeating the training process for multiple epochs.

---

# 15. Calculating a Sum With a Loop

Suppose:

```python
values = [2, 4, 6]
```

We can calculate the total manually using a loop:

```python
total = 0

for value in values:
    total = total + value

print(total)
```

Output:

```text
12
```

The value of `total` changes during each iteration.

---

# 16. Accumulation

Step by step:

```text
total = 0

value = 2
total = 0 + 2
total = 2

value = 4
total = 2 + 4
total = 6

value = 6
total = 6 + 6
total = 12
```

This process is called accumulation.

---

# 17. The `+=` Operator

Instead of:

```python
total = total + value
```

we can write:

```python
total += value
```

Both mean the same thing.

Example:

```python
x = 5
x += 2
```

The final value of `x` is:

```text
7
```

---

# 18. Calculating an Average With a Loop

Example:

```python
stress_levels = [3, 5, 7, 9]

total = 0

for stress in stress_levels:
    total += stress

average = total / len(stress_levels)

print("Average:", average)
```

Output:

```text
Average: 6.0
```

`len()` returns the number of elements.

For:

```python
[3, 5, 7, 9]
```

the result of:

```python
len(stress_levels)
```

is:

```text
4
```

---

# 19. Counting Values That Match a Condition

Suppose:

```python
stress_levels = [3, 8, 5, 9, 2, 7]
```

We can count high-stress values:

```python
high_stress_count = 0

for stress in stress_levels:
    if stress >= 7:
        high_stress_count += 1

print(high_stress_count)
```

Output:

```text
3
```

This type of counting is common when analyzing data.

---

# 20. The `while` Loop

A `while` loop continues while a condition remains true.

```python
number = 1

while number <= 5:
    print(number)
    number += 1
```

Output:

```text
1
2
3
4
5
```

The condition is checked before each iteration.

---

# 21. How `while` Works

Initially:

```python
number = 1
```

Python checks:

```python
number <= 5
```

If the condition is `True`, the loop runs.

Then:

```python
number += 1
```

changes the value.

Eventually:

```python
number = 6
```

and:

```python
6 <= 5
```

becomes:

```text
False
```

The loop stops.

---

# 22. Infinite Loops

This code causes a problem:

```python
number = 1

while number <= 5:
    print(number)
```

`number` never changes.

Therefore:

```python
number <= 5
```

remains true forever.

The program keeps running.

This is called an infinite loop.

A `while` loop should normally contain something that eventually makes its condition false.

---

# 23. `for` vs `while`

Use `for` when working through a known sequence or a known number of repetitions.

Example:

```python
for i in range(10):
    print(i)
```

Use `while` when repetition depends on a condition and the exact number of repetitions may not be known.

Example:

```python
while score < target:
    ...
```

---

# 24. Input Validation With `while`

A `while` loop can keep asking for input until a valid value is entered.

```python
stress_level = float(
    input("Enter stress level between 0 and 10: ")
)

while stress_level < 0 or stress_level > 10:
    print("Invalid value.")

    stress_level = float(
        input("Enter stress level between 0 and 10: ")
    )

print("Valid stress level:", stress_level)
```

---

# 25. Simple Data Processing Example

```python
stress_levels = [2, 8, 6, 9, 4]

for stress in stress_levels:
    if stress >= 7:
        print(stress, "→ High")
    elif stress >= 4:
        print(stress, "→ Moderate")
    else:
        print(stress, "→ Low")
```

Output:

```text
2 → Low
8 → High
6 → Moderate
9 → High
4 → Moderate
```

This is a simple example of processing several data samples one by one.

---

# Key Points

- A loop repeats code.
- `for` is useful for iterating over known data or a known number of repetitions.
- `while` repeats code while a condition remains true.
- `range()` generates sequences of integers.
- The stop value of `range()` is not included.
- `range(start, stop, step)` allows control over the generated sequence.
- Loops can contain conditions.
- Variables such as `total` and counters can accumulate information.
- `+=` is a shorter form of updating a variable.
- `len()` gives the number of elements.
- A `while` loop can become infinite if its condition never becomes false.
- Loops are fundamental for data processing and model-training workflows.
