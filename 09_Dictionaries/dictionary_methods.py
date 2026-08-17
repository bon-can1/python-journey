# Explore useful dictionary functions.
# Python provides many helpful dictionary methods
# keys() returns all dictionary keys
# values() returns all dictionary values
# items() returns all key-value pairs
# get() safely retrieves a value
# copy() creates a shallow copy
# setdefault() adds a key only if it does not exist


# example 1  keys, values, items
student = {
    "name": "Arun",
    "age": 20,
    "course": "Python"
}
print(student.keys())
print(student.values())
print(student.items())


# example 2  get with default
print(student.get("name"))
print(student.get("phone", "Not found"))


# example 3  copy dictionary
student_copy = student.copy()
print(student_copy)


# example 4  setdefault
student.setdefault("city", "Delhi")
student.setdefault("name", "Ravi")
print(student)


# example 5  len of dictionary
print("Total fields:", len(student))


# example 6  check key existence
print("name" in student)
print("phone" in student)


# example 7  loop with enumerate on items
for index, (key, value) in enumerate(student.items(), start=1):
    print(index, key, ":", value)


# ==========================================================
# MINI PROJECT 1
# STUDENT REPORT GENERATOR
# ==========================================================

# Display all student details in a formatted report using dictionary methods.

student = {
    "name": input("Enter name: "),
    "roll": int(input("Enter roll number: ")),
    "marks": float(input("Enter marks: ")),
    "course": input("Enter course: ")
}

print("\nStudent Report")
print("-" * 20)

for key, value in student.items():
    print(key.title() + ":", value)


# ==========================================================
# MINI PROJECT 2
# PRODUCT SEARCH SYSTEM
# ==========================================================

# Search for a product in a dictionary and show details if found.

products = {
    "Laptop": 45000,
    "Phone": 25000,
    "Tablet": 18000
}

search = input("Enter product name to search: ")

if search in products:
    print(f"{search} is available.")
    print("Price: Rs.", products[search])
else:
    print("Product not found.")
    print("Available products:", list(products.keys()))
