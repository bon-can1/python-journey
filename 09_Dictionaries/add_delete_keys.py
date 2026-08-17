# Add or remove entries.
# New key-value pairs can be added to a dictionary
# Assign a value to a new key to add an entry
# del removes a key-value pair completely
# pop() removes a key and returns its value
# popitem() removes the last inserted item
# clear() removes all entries from the dictionary


# example 1  add new key-value pair
student = {
    "name": "Arun",
    "age": 20
}
student["city"] = "Mumbai"
print(student)


# example 2  add using update()
student.update({"phone": "9876543210"})
print(student)


# example 3  delete using del
del student["phone"]
print(student)


# example 4  remove using pop()
removed_age = student.pop("age")
print("Removed:", removed_age)
print(student)


# example 5  remove safely with default
email = student.pop("email", "No email found")
print(email)


# example 6  clear dictionary
backup = student.copy()
student.clear()
print(student)


# ==========================================================
# MINI PROJECT 1
# PHONE BOOK MANAGER
# ==========================================================

# Add a new contact and delete an old contact from a phone book.

phonebook = {
    "Arun": "9876543210",
    "Priya": "9123456780"
}

print("Current Phonebook:", phonebook)

name = input("Enter new contact name: ")
number = input("Enter phone number: ")
phonebook[name] = number

remove_name = input("Enter contact name to delete: ")
phonebook.pop(remove_name, None)

print("\nUpdated Phonebook:", phonebook)


# ==========================================================
# MINI PROJECT 2
# TASK LIST MANAGER
# ==========================================================

# Add tasks to a dictionary and remove a completed task.

tasks = {
    "Task 1": "Pending",
    "Task 2": "Pending"
}

print("Current Tasks:", tasks)

task_name = input("Enter new task name: ")
tasks[task_name] = "Pending"

done_task = input("Enter completed task name: ")
tasks.pop(done_task, None)

print("\nUpdated Tasks:", tasks)
