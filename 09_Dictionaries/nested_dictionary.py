# Store dictionaries within dictionaries.
# A nested dictionary contains dictionaries as values
# Nested dictionaries are useful for complex structured data
# Access nested values using multiple keys
# Each level uses its own key
# Nested dictionaries are common in real-world applications


# example 1  basic nested dictionary
student = {
    "name": "Arun",
    "marks": {
        "math": 85,
        "science": 90,
        "english": 78
    }
}
print(student)
print(student["marks"]["math"])


# example 2  nested user profile
user = {
    "username": "coder123",
    "contact": {
        "email": "coder@gmail.com",
        "phone": "9876543210"
    },
    "address": {
        "city": "Bangalore",
        "pincode": 560001
    }
}
print(user["contact"]["email"])
print(user["address"]["city"])


# example 3  multiple students
students = {
    "s1": {"name": "Arun", "age": 20},
    "s2": {"name": "Priya", "age": 21},
    "s3": {"name": "Ravi", "age": 19}
}
print(students["s2"]["name"])


# example 4  update nested value
student["marks"]["english"] = 82
print(student["marks"])


# example 5  loop through nested dictionary
for subject, mark in student["marks"].items():
    print(subject, ":", mark)


# example 6  add new nested key
student["marks"]["history"] = 88
print(student["marks"])


# ==========================================================
# MINI PROJECT 1
# SCHOOL RECORD SYSTEM
# ==========================================================

# Store marks for multiple subjects inside one student dictionary.

student = {
    "name": input("Enter student name: "),
    "roll": int(input("Enter roll number: ")),
    "marks": {
        "math": int(input("Enter math marks: ")),
        "science": int(input("Enter science marks: ")),
        "english": int(input("Enter english marks: "))
    }
}

total = (
    student["marks"]["math"]
    + student["marks"]["science"]
    + student["marks"]["english"]
)

print("\nStudent Record")
print("Name:", student["name"])
print("Roll:", student["roll"])
print("Marks:", student["marks"])
print("Total:", total)


# ==========================================================
# MINI PROJECT 2
# EMPLOYEE DIRECTORY
# ==========================================================

# Store employee details with nested contact and job information.

employees = {
    "E101": {
        "name": "Arun",
        "job": {
            "role": "Developer",
            "salary": 50000
        },
        "contact": {
            "email": "arun@company.com",
            "phone": "9876543210"
        }
    },
    "E102": {
        "name": "Priya",
        "job": {
            "role": "Designer",
            "salary": 45000
        },
        "contact": {
            "email": "priya@company.com",
            "phone": "9123456780"
        }
    }
}

emp_id = input("Enter employee ID (E101 or E102): ")

if emp_id in employees:
    emp = employees[emp_id]
    print("\nEmployee Details")
    print("Name:", emp["name"])
    print("Role:", emp["job"]["role"])
    print("Salary:", emp["job"]["salary"])
    print("Email:", emp["contact"]["email"])
else:
    print("Employee ID not found.")
