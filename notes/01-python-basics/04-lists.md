# Lists — Lesson 04

## Overview

In this lesson, I learned how to store and work with multiple values using Python lists.

Lists are important for Data Science and Artificial Intelligence because they allow multiple data samples to be stored and processed together.

Topics covered:

- Creating lists
- List elements
- Indexing
- Negative indexing
- Modifying elements
- `len()`
- `append()`
- `insert()`
- `remove()`
- `pop()`
- `in`
- `not in`
- `min()`
- `max()`
- `sum()`
- `count()`
- `sort()`
- `sorted()`
- Slicing
- Lists with loops
- Building new lists from existing data

---

# 1. What Is a List?

A list stores multiple values inside one variable.

```python
stress_levels = [2, 8, 5, 9, 3, 7]
```

The variable `stress_levels` contains several numbers.

We can check its type:

```python
print(type(stress_levels))
```

Output:

```text
<class 'list'>
```

---

# 2. Why Lists Are Useful

Without a list:

```python
heart_rate_1 = 72
heart_rate_2 = 88
heart_rate_3 = 95
heart_rate_4 = 105
heart_rate_5 = 80
```

With a list:

```python
heart_rates = [72, 88, 95, 105, 80]
```

This is much easier to manage.

We can also process all values with a loop:

```python
for rate in heart_rates:
    print(rate)
```

---

# 3. List Elements

Each value inside a list is called an element.

```python
sleep_hours = [6, 7.5, 5, 8, 6.5]
```

The elements are:

```text
6
7.5
5
8
6.5
```

---

# 4. Indexing

Python starts counting list positions from `0`.

```python
stress_levels = [2, 8, 5, 9, 3]
```

Positions:

```text
value:   2   8   5   9   3
index:   0   1   2   3   4
```

Examples:

```python
print(stress_levels[0])
print(stress_levels[1])
print(stress_levels[3])
```

Outputs:

```text
2
8
9
```

---

# 5. Index Errors

Suppose:

```python
values = [10, 20, 30]
```

Valid indexes are:

```text
0
1
2
```

This is invalid:

```python
print(values[3])
```

It causes:

```text
IndexError
```

The last index is:

```text
number of elements - 1
```

---

# 6. Negative Indexing

Python can access elements from the end of a list using negative indexes.

```python
values = [10, 20, 30, 40]
```

Last element:

```python
print(values[-1])
```

Output:

```text
40
```

Second-to-last:

```python
print(values[-2])
```

Output:

```text
30
```

---

# 7. Modifying List Elements

Lists are mutable, meaning their values can be changed.

```python
stress_levels = [2, 5, 8]

stress_levels[1] = 6

print(stress_levels)
```

Output:

```text
[2, 6, 8]
```

---

# 8. `len()`

`len()` returns the number of elements.

```python
stress_levels = [2, 8, 5, 9, 3]

print(len(stress_levels))
```

Output:

```text
5
```

---

# 9. `append()`

`append()` adds one element to the end of a list.

```python
stress_levels = [2, 5, 8]

stress_levels.append(7)

print(stress_levels)
```

Output:

```text
[2, 5, 8, 7]
```

Example with new data:

```python
heart_rates = [72, 80, 91]

new_rate = 88

heart_rates.append(new_rate)
```

---

# 10. `insert()`

`insert()` adds a value at a specific position.

```python
values = [10, 20, 30]

values.insert(1, 15)

print(values)
```

Output:

```text
[10, 15, 20, 30]
```

General form:

```python
list.insert(index, value)
```

---

# 11. `remove()`

`remove()` deletes an element based on its value.

```python
values = [10, 20, 30, 20]

values.remove(20)

print(values)
```

Output:

```text
[10, 30, 20]
```

Only the first matching value is removed.

---

# 12. `pop()`

`pop()` removes an element based on its index.

```python
values = [10, 20, 30]

values.pop(1)

print(values)
```

Output:

```text
[10, 30]
```

Without an index:

```python
values.pop()
```

the final element is removed.

---

# 13. `remove()` vs `pop()`

```text
remove() → remove by value
pop()    → remove by index
```

Example:

```python
values.remove(20)
```

means:

Remove the value `20`.

But:

```python
values.pop(1)
```

means:

Remove the element at index `1`.

---

# 14. Checking Membership With `in`

```python
stress_levels = [2, 5, 8, 9]

print(8 in stress_levels)
```

Output:

```text
True
```

But:

```python
print(7 in stress_levels)
```

Output:

```text
False
```

It can also be used with `if`:

```python
if 8 in stress_levels:
    print("Stress level 8 exists")
```

---

# 15. `not in`

`not in` checks that an element does not exist.

```python
values = [1, 2, 3]

if 5 not in values:
    print("5 is not in the list")
```

---

# 16. `min()` and `max()`

```python
heart_rates = [72, 105, 88, 110, 95]

print(min(heart_rates))
print(max(heart_rates))
```

Output:

```text
72
110
```

These functions are useful in basic data analysis.

---

# 17. `sum()`

```python
sleep_hours = [6, 7, 5]

print(sum(sleep_hours))
```

Output:

```text
18
```

We can calculate an average:

```python
average = sum(sleep_hours) / len(sleep_hours)
```

---

# 18. Calculating an Average

```python
stress_levels = [2, 8, 5, 9, 3]

average = sum(stress_levels) / len(stress_levels)

print(average)
```

---

# 19. `count()`

`count()` returns how many times a value appears.

```python
labels = [0, 1, 1, 0, 1, 1, 1]

print(labels.count(1))
```

Output:

```text
5
```

Example related to classification:

```python
labels = [0, 1, 1, 0, 1]

stress_cases = labels.count(1)
normal_cases = labels.count(0)

print(stress_cases)
print(normal_cases)
```

This is a simple way to examine class distribution.

---

# 20. `sort()`

`sort()` sorts the original list.

```python
stress_levels = [8, 2, 9, 4, 5]

stress_levels.sort()

print(stress_levels)
```

Output:

```text
[2, 4, 5, 8, 9]
```

Descending order:

```python
stress_levels.sort(reverse=True)
```

Output:

```text
[9, 8, 5, 4, 2]
```

---

# 21. `sort()` vs `sorted()`

```python
values.sort()
```

changes the original list.

But:

```python
sorted(values)
```

returns a new sorted version.

---

# 22. Slicing

Slicing allows us to select part of a list.

```python
values = [10, 20, 30, 40, 50]
```

Example:

```python
values[1:4]
```

Result:

```text
[20, 30, 40]
```

The rule is:

```text
start → included
stop  → excluded
```

---

# 23. Slicing From the Beginning

```python
values[:3]
```

Result:

```text
[10, 20, 30]
```

---

# 24. Slicing to the End

```python
values[2:]
```

Result:

```text
[30, 40, 50]
```

---

# 25. Slicing and AI/Data

Suppose a dataset contains 100 samples.

Conceptually:

```python
training_data = data[:80]
test_data = data[80:]
```

This uses the first 80 samples for training and the remaining samples for testing.

In real Machine Learning projects, dedicated tools such as `train_test_split()` are usually used instead.

---

# 26. Lists and Loops

Lists work naturally with loops.

```python
stress_levels = [2, 8, 5, 9, 3]

for stress in stress_levels:
    print(stress)
```

We can also use conditions:

```python
for stress in stress_levels:
    if stress >= 7:
        print(stress, "High")
    else:
        print(stress, "Normal")
```

---

# 27. Building a New List

We can create an empty list:

```python
high_stress_levels = []
```

Then add values that satisfy a condition:

```python
stress_levels = [2, 8, 5, 9, 3]

high_stress_levels = []

for stress in stress_levels:
    if stress >= 7:
        high_stress_levels.append(stress)

print(high_stress_levels)
```

Output:

```text
[8, 9]
```

This is a common data-processing pattern:

```text
read data
↓
check condition
↓
keep useful values
```

---

# 28. Data Example

```python
heart_rates = [72, 105, 88, 110, 95, 68]

high_heart_rates = []

for rate in heart_rates:
    if rate > 100:
        high_heart_rates.append(rate)

print(high_heart_rates)
print("Number:", len(high_heart_rates))
```

Output:

```text
[105, 110]
Number: 2
```

---

# 29. Lists Can Contain Different Data Types

Python allows:

```python
data = ["Mohammad", 25, 8.5, True]
```

However, in Data Science it is often easier to work with collections that contain values with a consistent meaning.

For example:

```python
heart_rates = [72, 80, 95, 100]
```

is generally more useful for numerical analysis than:

```python
heart_rates = [72, "hello", True, 95]
```

---

# Key Points

- Lists store multiple values.
- List indexes start at `0`.
- Negative indexes access values from the end.
- Lists can be modified.
- `len()` returns the number of elements.
- `append()` adds to the end.
- `insert()` adds at a chosen index.
- `remove()` removes by value.
- `pop()` removes by index.
- `in` and `not in` check membership.
- `min()` and `max()` find extreme values.
- `sum()` calculates a total.
- `count()` counts occurrences.
- `sort()` modifies the original list.
- `sorted()` returns a sorted version.
- Slicing selects a portion of a list.
- Lists and loops can be combined to filter and process data.
