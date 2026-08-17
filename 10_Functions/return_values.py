# Send data back from functions.
# return sends a value back to the caller
# A function can return numbers, strings, lists, and more
# Without return, a function returns None by default
# Returned values can be stored in variables
# return stops the function immediately


# example 1  return a number
def add(a, b):
    return a + b

result = add(10, 20)
print(result)


# example 2  return a string
def full_name(first, last):
    return first + " " + last

name = full_name("Arun", "Kumar")
print(name)


# example 3  return multiple values as a tuple
def get_min_max(numbers):
    return min(numbers), max(numbers)

data = [5, 12, 3, 9, 18]
minimum, maximum = get_min_max(data)
print("Min:", minimum, "Max:", maximum)


# example 4  return early from a function
def check_even(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

print(check_even(4))
print(check_even(7))


# example 5  function without return gives None
def show_text(text):
    print(text)

value = show_text("Hello")
print("Returned value:", value)


# ==========================================================
# MINI PROJECT 1
# DISCOUNT CALCULATOR
# ==========================================================

# Calculate final price after applying a discount percentage.

def apply_discount(price, discount_percent):
    discount = price * discount_percent / 100
    final_price = price - discount
    return final_price

original = float(input("Enter original price: "))
discount = float(input("Enter discount percentage: "))
final = apply_discount(original, discount)

print("Original Price:", original)
print("Final Price:", final)


# ==========================================================
# MINI PROJECT 2
# GRADE FINDER
# ==========================================================

# Return a letter grade based on marks.

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    return "F"

marks = float(input("Enter marks: "))
grade = get_grade(marks)
print(f"Marks: {marks} -> Grade: {grade}")
