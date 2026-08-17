# Handle unlimited positional arguments.
# *args collects extra positional arguments into a tuple
# The name args is a convention; only the * matters
# Useful when the number of inputs is unknown
# *args must come after regular parameters
# You can loop through args like any tuple


# example 1  basic *args
def show_numbers(*args):
    print("Received:", args)

show_numbers(1, 2, 3)
show_numbers(10, 20, 30, 40)


# example 2  loop through *args
def print_all(*args):
    for item in args:
        print(item)

print_all("Python", "Java", "C++")


# example 3  sum all numbers in *args
def add_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(add_all(5, 10, 15))
print(add_all(1, 2, 3, 4, 5))


# example 4  mix regular parameter with *args
def greet_leader(leader, *members):
    print("Leader:", leader)
    print("Members:", members)

greet_leader("Arun", "Priya", "Ravi", "Kiran")


# example 5  find maximum value using *args
def find_max(*values):
    if len(values) == 0:
        return None
    maximum = values[0]
    for value in values:
        if value > maximum:
            maximum = value
    return maximum

print(find_max(3, 9, 1, 7))
print(find_max(45, 12, 88, 33))


# ==========================================================
# MINI PROJECT 1
# SHOPPING TOTAL CALCULATOR
# ==========================================================

# Calculate total price from any number of item prices.

def calculate_total(*prices):
    total = 0
    for price in prices:
        total += price
    return total

print("Enter item prices separated by commas.")
price_input = input("Prices: ")
price_list = [float(p.strip()) for p in price_input.split(",")]

total_bill = calculate_total(*price_list)
print("Total Bill: Rs.", total_bill)


# ==========================================================
# MINI PROJECT 2
# CLASS AVERAGE FINDER
# ==========================================================

# Find average marks from multiple student scores.

def average_marks(*marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

print("Enter marks separated by commas.")
marks_input = input("Marks: ")
marks_list = [float(m.strip()) for m in marks_input.split(",")]

avg = average_marks(*marks_list)
print("Average Marks:", round(avg, 2))
