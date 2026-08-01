# Store multiple values together.
# Tuple packing means putting multiple values into a single tuple
# Python automatically packs values when separated by commas
# Parentheses are optional during packing
# Packing is useful for returning multiple values from data
# Packed tuples keep values in a fixed order
# Packing helps group related data together


# example 1  basic packing
point = 10, 20, 30
print(point)
print(type(point))


# example 2  packing with parentheses
student = ("Arun", 20, "India")
print(student)


# example 3  packing mixed data types
record = (
    "Laptop",
    45000,
    True
)
print(record)


# example 4  packing from variables
name = "Priya"
age = 22
city = "Mumbai"
profile = name, age, city
print(profile)


# example 5  nested packing
location = (
    (12.9716, 77.5946),
    (28.6139, 77.2090)
)
print(location)


# ==========================================================
# MINI PROJECT 1
# STUDENT RECORD PACKER
# ==========================================================

# Pack student name, roll number, and marks into one tuple.

name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
marks = float(input("Enter marks: "))

student_record = name, roll, marks

print("\nPacked Student Record")
print(student_record)


# ==========================================================
# MINI PROJECT 2
# BOOK INFO PACKER
# ==========================================================

# Pack book title, author, and price into a tuple and display each field.

title = input("Enter book title: ")
author = input("Enter author name: ")
price = float(input("Enter book price: "))

book = title, author, price

print("\nBook Details")
print("Title:", book[0])
print("Author:", book[1])
print("Price:", book[2])
