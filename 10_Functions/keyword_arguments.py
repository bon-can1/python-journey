# Pass arguments by name.
# Keyword arguments use parameter names when calling a function
# Order does not matter when using keyword arguments
# Positional arguments must come before keyword arguments
# Keyword arguments make function calls more readable
# Useful when a function has many parameters


# example 1  basic keyword arguments
def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

introduce(name="Arun", age=20, city="Delhi")
introduce(city="Chennai", name="Priya", age=22)


# example 2  mix positional and keyword arguments
def order_food(item, quantity, price):
    total = quantity * price
    print(f"Ordered {quantity} {item}(s) for Rs. {total}")

order_food("Pizza", quantity=2, price=250)
order_food("Burger", 3, price=120)


# example 3  keyword arguments with defaults
def send_email(recipient, subject, body="No message"):
    print("To:", recipient)
    print("Subject:", subject)
    print("Body:", body)

send_email(recipient="admin@example.com", subject="Hello")
send_email("user@example.com", "Update", body="Your account is active.")


# example 4  readable function call with many parameters
def register_student(name, roll, course, year, city):
    print("Registration Successful")
    print(name, roll, course, year, city)

register_student(
    name="Ravi",
    roll=105,
    course="Python",
    year=1,
    city="Bangalore"
)


# example 5  avoid confusion with keyword arguments
def divide(a, b):
    return a / b

print(divide(a=10, b=2))
print(divide(b=5, a=20))


# ==========================================================
# MINI PROJECT 1
# EMPLOYEE DETAILS PRINTER
# ==========================================================

# Display employee details using keyword arguments.

def show_employee(name, department, salary, location):
    print("\n--- Employee Record ---")
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)
    print("Location:", location)

show_employee(
    name=input("Enter name: "),
    department=input("Enter department: "),
    salary=float(input("Enter salary: ")),
    location=input("Enter location: ")
)


# ==========================================================
# MINI PROJECT 2
# EVENT BOOKING SYSTEM
# ==========================================================

# Book an event using keyword arguments for clarity.

def book_event(event_name, date, seats, venue="Main Hall"):
    print("\nEvent Booked Successfully")
    print("Event:", event_name)
    print("Date:", date)
    print("Seats:", seats)
    print("Venue:", venue)

book_event(
    event_name=input("Enter event name: "),
    date=input("Enter date: "),
    seats=int(input("Enter number of seats: "))
)
