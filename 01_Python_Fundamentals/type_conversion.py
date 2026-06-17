# Convert data between different types.

a = 10
print(type(a))  # int

# int to string
b = str(a)
print(b, type(b))
print("The number is " + b)

# int to float
c = float(a)
print(c, type(c))

# string to int
text = "25"
d = int(text)
print(d, type(d))
print(d + 5)

# string to float
price = "9.99"
e = float(price)
print(e, type(e))

# int/float to bool — 0 is False, any other number is True
print(bool(0))    # False
print(bool(1))    # True
print(bool(42))   # True
print(bool(""))   # empty string is False
print(bool("hi")) # non-empty string is True

# you cannot add a string and an integer directly
# print("hello " + a)  # TypeError
# fix it by converting first:
print("hello " + str(a))
