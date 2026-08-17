# Store key-value pairs.
# A dictionary stores data as key-value pairs
# Keys must be unique
# Keys are usually strings or numbers
# Values can be any data type
# Dictionaries are mutable
# Dictionaries use curly braces {}
# Dictionaries are useful for storing labeled information


# example 1  basic dictionary
student = {
    "name": "Arun",
    "age": 20,
    "course": "Python"
}
print(student)


# example 2  mixed value types
profile = {
    "username": "coder123",
    "score": 95,
    "active": True
}
print(profile)


# example 3  empty dictionary
data = {}
print(data)


# example 4  create using dict()
person = dict(name="Priya", city="Delhi", age=22)
print(person)


# example 5  duplicate keys keep the last value
info = {
    "color": "red",
    "color": "blue"
}
print(info)


# example 6  nested dictionary preview
company = {
    "name": "TechCorp",
    "employees": 50,
    "location": {
        "city": "Bangalore",
        "country": "India"
    }
}
print(company)


# ==========================================================
# MINI PROJECT 1
# STUDENT PROFILE CREATOR
# ==========================================================

# Create a student dictionary using user input.

student = {
    "name": input("Enter name: "),
    "roll": int(input("Enter roll number: ")),
    "marks": float(input("Enter marks: "))
}

print("\nStudent Profile")
print(student)


# ==========================================================
# MINI PROJECT 2
# PRODUCT CATALOG ENTRY
# ==========================================================

# Store product name, price, and stock in a dictionary.

product = {
    "name": input("Enter product name: "),
    "price": float(input("Enter price: ")),
    "stock": int(input("Enter stock quantity: "))
}

print("\nProduct Added")
print("Name:", product["name"])
print("Price:", product["price"])
print("Stock:", product["stock"])
