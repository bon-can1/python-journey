# Create reusable blocks of code.
# A function is a named block of code that performs a task
# Use def to define a function
# Call a function by writing its name followed by ()
# Functions reduce repetition and keep code organized
# Functions can be called multiple times
# Code inside a function runs only when it is called


# example 1  simple function with no parameters
def greet():
    print("Hello, welcome to Python!")

greet()


# example 2  function called multiple times
def show_line():
    print("--------------------")

show_line()
print("Python Functions")
show_line()


# example 3  function with one parameter
def greet_person(name):
    print("Hello,", name)

greet_person("Arun")
greet_person("Priya")


# example 4  function with multiple parameters
def add_numbers(a, b):
    print(a, "+", b, "=", a + b)

add_numbers(10, 5)
add_numbers(3, 7)


# example 5  function with a docstring
def describe_python():
    """Print a short description of Python."""
    print("Python is easy to read and write.")

describe_python()
print(describe_python.__doc__)


# ==========================================================
# MINI PROJECT 1
# GREETING GENERATOR
# ==========================================================

# Create a function that greets a user by name.

def welcome_user():
    name = input("Enter your name: ")
    print(f"Welcome, {name}! Glad to have you here.")

welcome_user()


# ==========================================================
# MINI PROJECT 2
# AREA CALCULATOR
# ==========================================================

# Calculate the area of a rectangle using a function.

def rectangle_area(length, width):
    area = length * width
    print(f"Area of rectangle: {area}")

length = float(input("Enter length: "))
width = float(input("Enter width: "))
rectangle_area(length, width)
