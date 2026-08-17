# Handle unlimited keyword arguments.
# **kwargs collects extra keyword arguments into a dictionary
# The name kwargs is a convention; only the ** matters
# Useful when keyword names and values are not known in advance
# **kwargs must come after regular parameters and *args
# You can loop through kwargs using .items()


# example 1  basic **kwargs
def show_details(**kwargs):
    print(kwargs)

show_details(name="Arun", age=20, city="Delhi")


# example 2  loop through **kwargs
def print_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_profile(name="Priya", course="Python", marks=88)


# example 3  mix regular parameter with **kwargs
def create_user(username, **extra_data):
    profile = {"username": username}
    profile.update(extra_data)
    return profile

user = create_user("coder123", email="coder@mail.com", active=True)
print(user)


# example 4  function with *args and **kwargs
def demo_function(title, *args, **kwargs):
    print("Title:", title)
    print("Args:", args)
    print("Kwargs:", kwargs)

demo_function("Demo", 1, 2, 3, color="blue", size="large")


# example 5  build a settings dictionary
def configure_app(**settings):
    defaults = {"theme": "light", "language": "en"}
    defaults.update(settings)
    return defaults

app_settings = configure_app(theme="dark", notifications=True)
print(app_settings)


# ==========================================================
# MINI PROJECT 1
# STUDENT PROFILE BUILDER
# ==========================================================

# Build a student profile using any number of keyword fields.

def build_student_profile(name, roll, **extra_info):
    profile = {"name": name, "roll": roll}
    profile.update(extra_info)
    return profile

name = input("Enter name: ")
roll = int(input("Enter roll number: "))
city = input("Enter city (optional): ")
phone = input("Enter phone (optional): ")

profile = build_student_profile(
    name,
    roll,
    city=city,
    phone=phone
)

print("\nStudent Profile:")
for key, value in profile.items():
    print(f"{key}: {value}")


# ==========================================================
# MINI PROJECT 2
# PRODUCT INFO DISPLAY
# ==========================================================

# Display product details passed as keyword arguments.

def show_product(name, price, **details):
    print("\n--- Product Details ---")
    print("Name:", name)
    print("Price: Rs.", price)
    for key, value in details.items():
        print(f"{key}: {value}")

show_product(
    name=input("Enter product name: "),
    price=float(input("Enter price: ")),
    brand=input("Enter brand: "),
    warranty=input("Enter warranty: "),
    stock=int(input("Enter stock: "))
)
