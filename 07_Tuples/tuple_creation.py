# Create immutable collections.
# A tuple is used to store multiple values in one variable
# Tuples are ordered
# Tuples allow duplicate values
# Tuples can store different data types
# Tuples are IMMUTABLE
# Immutable means the tuple cannot be changed after creation
# Tuples normally use parentheses ()
#
# List  -> Mutable   -> Can change
# Tuple -> Immutable -> Cannot change


# example 1  integer tuple
num = (10, 20, 30, 40)
print(num)

# EXAMPLE 2  STRING TUPLE
languages = ("Python", "Java", "C++")
print(languages)


# EXAMPLE 3  MIXED DATA TYPES
student = (
    "Arun",
    20,
    6.53,
    True
)
print(student)

# EXAMPLE 4  EMPTY TUPLE
data = ()
print(data)
print(type(data))


# EXAMPLE 5  single element tuple
number = (10,)# The comma creates the single-element tuple otherwise it will integer
print(number)
print(type(number))



# ==========================================================
# MINI PROJECT 1
# GPS LOCATION STORAGE
# ==========================================================

# Store a fixed GPS location using a tuple.

latitude = float(
    input("Enter latitude: ")
)
longitude = float(
    input("Enter longitude: ")
)
location = (
    latitude,
    longitude
)
print("\nSaved GPS Location")
print(location)
print("Data Type:", type(location))


# ==========================================================
# MINI PROJECT 2
# RGB COLOR STORAGE
# ==========================================================

# Store a fixed RGB color using a tuple.
# RGB values must stay between 0 and 255.

red = int(input("Enter red value (0-255): "))
green = int(input("Enter green value (0-255): "))
blue = int(input("Enter blue value (0-255): "))

color = (red, green, blue)

print("\nSaved RGB Color")
print("Red:", color[0])
print("Green:", color[1])
print("Blue:", color[2])
print("Full Tuple:", color)