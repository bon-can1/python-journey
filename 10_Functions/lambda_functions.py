# Create small anonymous functions.
# lambda creates a small function without using def
# lambda is useful for one-line simple operations
# Syntax: lambda parameters: expression
# lambda functions are often used with map(), filter(), and sorted()
# lambda functions can take any number of arguments but only one expression


# example 1  basic lambda function
square = lambda x: x * x
print(square(5))
print(square(9))


# example 2  lambda with two parameters
add = lambda a, b: a + b
print(add(10, 20))


# example 3  lambda with sorted()
students = [
    ("Arun", 85),
    ("Priya", 92),
    ("Ravi", 78)
]
sorted_by_marks = sorted(students, key=lambda student: student[1], reverse=True)
print(sorted_by_marks)


# example 4  lambda with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda n: n * n, numbers))
print(squares)


# example 5  lambda with filter()
values = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda n: n % 2 == 0, values))
print(evens)


# ==========================================================
# MINI PROJECT 1
# PRICE DISCOUNT APPLIER
# ==========================================================

# Apply a 10% discount to all prices using lambda and map().

prices = [100, 250, 400, 150, 300]
discounted = list(map(lambda price: price * 0.9, prices))

print("Original Prices:", prices)
print("Discounted Prices:", discounted)


# ==========================================================
# MINI PROJECT 2
# PASSING STUDENTS FILTER
# ==========================================================

# Filter students who scored 40 or above using lambda and filter().

students = {
    "Arun": 35,
    "Priya": 78,
    "Ravi": 42,
    "Kiran": 28,
    "Meera": 91
}

passing = dict(filter(lambda item: item[1] >= 40, students.items()))

print("All Students:", students)
print("Passing Students:", passing)
