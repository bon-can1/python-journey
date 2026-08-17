# Pass data into functions.
# Parameters are variables listed in the function definition
# Arguments are the actual values passed when calling a function
# Positional arguments are matched by order
# You can pass strings, numbers, lists, and other data types
# Parameters make functions flexible and reusable


# example 1  single parameter
def print_message(msg):
    print("Message:", msg)

print_message("Learning Python is fun!")


# example 2  multiple parameters
def show_student(name, roll, marks):
    print("Name:", name)
    print("Roll:", roll)
    print("Marks:", marks)

show_student("Arun", 101, 85)


# example 3  pass different data types
def display_info(title, count, active):
    print("Title:", title)
    print("Count:", count)
    print("Active:", active)

display_info("Python Course", 25, True)


# example 4  pass a list as parameter
def show_items(items):
    for item in items:
        print("-", item)

fruits = ["apple", "banana", "mango"]
show_items(fruits)


# example 5  pass a dictionary as parameter
def show_profile(profile):
    for key, value in profile.items():
        print(key, ":", value)

student = {"name": "Priya", "age": 20, "city": "Delhi"}
show_profile(student)


# ==========================================================
# MINI PROJECT 1
# BILL PRINTER
# ==========================================================

# Print a bill using a function with item name, quantity, and price.

def print_bill(item, quantity, price):
    total = quantity * price
    print("\n--- BILL ---")
    print("Item:", item)
    print("Quantity:", quantity)
    print("Price per unit:", price)
    print("Total:", total)

item = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per unit: "))
print_bill(item, quantity, price)


# ==========================================================
# MINI PROJECT 2
# TEMPERATURE CONVERTER
# ==========================================================

# Convert Celsius to Fahrenheit using a function parameter.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")

temp = float(input("Enter temperature in Celsius: "))
celsius_to_fahrenheit(temp)
