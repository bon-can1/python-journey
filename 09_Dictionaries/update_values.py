# Modify existing data.
# Dictionary values can be changed after creation
# Assign a new value to an existing key to update it
# update() can modify multiple values at once
# Keys stay the same unless you rename them separately
# Updating is useful when information changes over time


# example 1  update single value
student = {
    "name": "Arun",
    "age": 20,
    "marks": 75
}
student["marks"] = 88
print(student)


# example 2  update multiple values using update()
student.update({
    "age": 21,
    "city": "Delhi"
})
print(student)


# example 3  update nested value
company = {
    "name": "TechCorp",
    "employees": 50
}
company["employees"] = 55
print(company)


# example 4  increment numeric value
scores = {"math": 70, "science": 80}
scores["math"] = scores["math"] + 5
print(scores)


# example 5  change string value
user = {"username": "old_name", "status": "offline"}
user["status"] = "online"
print(user)


# ==========================================================
# MINI PROJECT 1
# MARK UPDATER
# ==========================================================

# Update a student's marks after re-evaluation.

student = {
    "name": "Kiran",
    "roll": 101,
    "marks": 72
}

print("Before Update:", student)

new_marks = float(input("Enter updated marks: "))
student["marks"] = new_marks

print("After Update:", student)


# ==========================================================
# MINI PROJECT 2
# INVENTORY STOCK UPDATE
# ==========================================================

# Reduce product stock after a sale.

inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

print("Current Inventory:", inventory)

product = input("Enter product sold: ")
quantity = int(input("Enter quantity sold: "))

if product in inventory:
    inventory[product] = inventory[product] - quantity
    print("Updated Inventory:", inventory)
else:
    print("Product not found in inventory.")
