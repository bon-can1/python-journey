# Test if values exist in collections.
# membership operators: in and not in

fruits = ["apple", "banana", "mango"]
text = "Python is fun"

# in — checks if a value exists
print("apple in fruits:", "apple" in fruits)       # True
print("grape in fruits:", "grape" in fruits)       # False

# not in — checks if a value does NOT exist
print("grape not in fruits:", "grape" not in fruits)   # True
print("apple not in fruits:", "apple" not in fruits)   # False

# works with strings (checks for substrings)
print("'fun' in text:", "fun" in text)             # True
print("'java' in text:", "java" in text)           # False

# works with tuples and sets
numbers = (1, 2, 3, 4, 5)
print("3 in numbers:", 3 in numbers)               # True

unique = {10, 20, 30}
print("20 in unique:", 20 in unique)               # True

# works with dictionaries — checks keys, not values
person = {"name": "Arun", "age": 20}
print("'name' in person:", "name" in person)       # True
print("'Arun' in person:", "Arun" in person)       # False (Arun is a value, not a key)
