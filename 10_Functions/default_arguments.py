# Use default parameter values.
# Default values are used when an argument is not provided
# Default parameters must come after non-default parameters
# Defaults make functions easier to use with optional settings
# You can still override defaults by passing a value
# Default values are evaluated once when the function is defined


# example 1  single default parameter
def greet(name, message="Hello"):
    print(message + ",", name)

greet("Arun")
greet("Priya", "Welcome")


# example 2  multiple default parameters
def create_profile(name, age=18, city="Unknown"):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

create_profile("Ravi")
create_profile("Kiran", 22)
create_profile("Meera", 25, "Chennai")


# example 3  default with calculation
def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))


# example 4  default list parameter (safe pattern)
def add_item(item, shopping_list=None):
    if shopping_list is None:
        shopping_list = []
    shopping_list.append(item)
    return shopping_list

list_a = add_item("Apple")
list_b = add_item("Banana")
print(list_a)
print(list_b)


# example 5  mix required and optional parameters
def book_ticket(movie, seats=1, price=150):
    total = seats * price
    print(f"Movie: {movie}, Seats: {seats}, Total: Rs. {total}")

book_ticket("Inception")
book_ticket("Interstellar", 3)
book_ticket("Avatar", 2, 200)


# ==========================================================
# MINI PROJECT 1
# SHIPPING COST CALCULATOR
# ==========================================================

# Calculate shipping cost with a default delivery fee.

def calculate_shipping(weight, rate=10, base_fee=50):
    cost = base_fee + (weight * rate)
    return cost

weight = float(input("Enter package weight (kg): "))
total = calculate_shipping(weight)

print(f"Shipping cost for {weight} kg: Rs. {total}")


# ==========================================================
# MINI PROJECT 2
# CUSTOM GREETING APP
# ==========================================================

# Greet users with a custom or default message.

def custom_greet(name, greeting="Good Morning"):
    return f"{greeting}, {name}!"

name = input("Enter your name: ")
message = input("Enter greeting (press Enter for default): ")

if message.strip() == "":
    print(custom_greet(name))
else:
    print(custom_greet(name, message))
