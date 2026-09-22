# Python for AI Learning
# Lesson 01 - Python Fundamentals


# ==========================================
# Exercise 1 - Variables
# ==========================================

name = "Mohammad"
age = 25
field = "Artificial Intelligence"

print("Exercise 1")
print(name)
print(age)
print(field)

print()


# ==========================================
# Exercise 2 - Arithmetic Operations
# ==========================================

a = 15
b = 4

print("Exercise 2")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Exponentiation:", a ** b)

print()


# ==========================================
# Exercise 3 - Average Sleep
# ==========================================

sleep_day1 = 6.5
sleep_day2 = 7
sleep_day3 = 5.5

average_sleep = (sleep_day1 + sleep_day2 + sleep_day3) / 3

print("Exercise 3")
print("Average sleep:", average_sleep)

print()


# ==========================================
# Exercise 4 - User Input
# ==========================================

sleep_hours = float(
    input("How many hours did you sleep last night? ")
)

print("Exercise 4")
print("You slept", sleep_hours, "hours.")

print()


# ==========================================
# Exercise 5 - Simple AI-Related Data
# ==========================================

heart_rate = 90
sleep_hours = 5
stress_score = 8

average_value = (
    heart_rate + sleep_hours + stress_score
) / 3

print("Exercise 5")
print("Average value:", average_value)
print("Data type:", type(average_value))