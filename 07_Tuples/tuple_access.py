# Access tuple elements
# Tuple access means retrieving values from a tuple
# Every tuple element has an index
# Python indexing starts from 0
# Positive indexing accesses values from the beginning
# Negative indexing accesses values from the end
# Tuple values can be read but cannot be reassigned
# Nested tuple elements can be accessed using multiple indexes


# example 1  positive indexing
fruit = ('apple', 'banana', 'mango', 'orange')
print(fruit[0])
print(fruit[2])
print(fruit[3])

# negative indexing
print(fruit[-1])
print(fruit[-3])
print(fruit[-2])




# ==========================================================
# MINI PROJECT 1
# FIXED PRODUCT VIEWER
# ==========================================================

products = (
    "Laptop",
    "Phone",
    "Keyboard",
    "Mouse",
    "Monitor"
)

print("Available Products")

for index, product in enumerate(
    products,
    start=1
):

    print(index, product)

choice = int(
    input("Select product number: ")
)

index = choice - 1

if 0 <= index < len(products):

    print(
        "Selected Product:",
        products[index]
    )

else:

    print("Invalid Product Number")


# ==========================================================
# MINI PROJECT 2
# STUDENT MARK VIEWER
# ==========================================================

# Access marks from a fixed student tuple using positive indexing.

student = (
    "Kiran",
    19,
    85,
    90,
    78
)

print("Student Name:", student[0])
print("Age:", student[1])
print("Math:", student[2])
print("Science:", student[3])
print("English:", student[4])

total = student[2] + student[3] + student[4]
average = total / 3

print("Total Marks:", total)
print("Average:", average)
