# Retrieve values using keys.
# Dictionary values are accessed using keys, not indexes
# Use square brackets [] to access a value by key
# Use get() for safe access with a default value
# keys() returns all keys
# values() returns all values
# items() returns key-value pairs together


# example 1  access using square brackets
student = {
    "name": "Arun",
    "age": 20,
    "city": "Chennai"
}
print(student["name"])
print(student["age"])


# example 2  access using get()
print(student.get("city"))
print(student.get("phone", "Not Available"))


# example 3  get all keys
print(student.keys())


# example 4  get all values
print(student.values())


# example 5  get all items
print(student.items())


# example 6  loop through dictionary
for key in student:
    print(key, ":", student[key])


# example 7  loop using items()
for key, value in student.items():
    print(key, "->", value)


# ==========================================================
# MINI PROJECT 1
# CONTACT LOOKUP
# ==========================================================

# Look up a phone number using a contact name as the key.

contacts = {
    "Arun": "9876543210",
    "Priya": "9123456780",
    "Ravi": "9988776655"
}

name = input("Enter contact name: ")

if name in contacts:
    print("Phone:", contacts[name])
else:
    print("Contact not found.")


# ==========================================================
# MINI PROJECT 2
# MENU PRICE CHECKER
# ==========================================================

# Display the price of a food item selected by the user.

menu = {
    "Pizza": 250,
    "Burger": 120,
    "Pasta": 180,
    "Sandwich": 90
}

print("Available Items:", list(menu.keys()))
item = input("Enter food item: ")

price = menu.get(item)

if price is not None:
    print(f"{item} costs Rs. {price}")
else:
    print("Item not available on menu.")
