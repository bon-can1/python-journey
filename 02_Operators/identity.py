# Check whether objects share memory.
# identity operators: is and is not

a = [1, 2, 3]
b = [1, 2, 3]
c = a

# == checks if values are equal
print("a == b:", a == b)   # True (same content)

# is checks if both variables point to the SAME object in memory
print("a is b:", a is b)   # False (different list objects)
print("a is c:", a is c)   # True (c points to the same list as a)

# is not — opposite of is
print("a is not b:", a is not b)   # True
print("a is not c:", a is not c)   # False

# common use: check for None
value = None
print("value is None:", value is None)
print("value is not None:", value is not None)

# integers and small strings are often cached by Python
x = 10
y = 10
print("x is y:", x is y)   # True for small integers
