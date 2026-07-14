# Create lists efficiently in one line
# List comprehension is a short way to create a new list
# It combines a loop and list creation in one line
# It can also contain conditions
# It reduces unnecessary lines of code
# It returns a NEW list
# It is commonly used in Python programs

# example 1 create number list
n = [i for i in range(1, 11)]
print(n)

# example 2  square of number
sq = [i * i for i in range(1, 11)]
print(sq)

# example 3  even number
even_numbers = [
    i for i in range(1, 21)
    if i % 2 == 0
]

print(even_numbers)