# Assign tuple values to variables.
# Tuple unpacking means assigning tuple elements to separate variables
# The number of variables must match the number of values
# Unpacking makes code cleaner and easier to read
# The asterisk (*) can capture remaining values
# Unpacking is commonly used with functions and loops
# Unpacking works because tuples are ordered collections


# example 1  basic unpacking
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x)
print(y)
print(z)


# example 2  unpacking string tuple
colors = ("red", "green", "blue")
first, second, third = colors
print(first)
print(second)
print(third)


# example 3  unpacking mixed data
student = ("Ravi", 21, 8.5)
name, age, gpa = student
print("Name:", name)
print("Age:", age)
print("GPA:", gpa)


# example 4  unpacking with asterisk
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first)
print(middle)
print(last)


# example 5  swap values using unpacking
a = 10
b = 20
a, b = b, a
print("a:", a)
print("b:", b)


# ==========================================================
# MINI PROJECT 1
# CONTACT UNPACKER
# ==========================================================

# Store contact details in a tuple and unpack into name, phone, and email.

contact = (
    input("Enter name: "),
    input("Enter phone: "),
    input("Enter email: ")
)

name, phone, email = contact

print("\nContact Details")
print("Name:", name)
print("Phone:", phone)
print("Email:", email)


# ==========================================================
# MINI PROJECT 2
# DATE UNPACKER
# ==========================================================

# Pack day, month, and year into a tuple, then unpack and print a formatted date.

day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

date = day, month, year
d, m, y = date

print(f"\nFormatted Date: {d}/{m}/{y}")
