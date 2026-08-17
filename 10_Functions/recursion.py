# Functions calling themselves.
# Recursion is when a function calls itself
# Every recursive function needs a base case to stop
# Without a base case, recursion runs forever
# Recursion is useful for problems that repeat in smaller parts
# Common examples: factorial, Fibonacci, and countdown


# example 1  simple countdown
def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)


# example 2  factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(6))


# example 3  sum of numbers using recursion
def sum_upto(n):
    if n == 0:
        return 0
    return n + sum_upto(n - 1)

print(sum_upto(10))


# example 4  Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")
print()


# example 5  reverse a string using recursion
def reverse_string(text):
    if len(text) == 0:
        return text
    return reverse_string(text[1:]) + text[0]

print(reverse_string("Python"))


# ==========================================================
# MINI PROJECT 1
# POWER CALCULATOR
# ==========================================================

# Calculate base raised to exponent using recursion.

def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
result = power(base, exponent)

print(f"{base} raised to {exponent} = {result}")


# ==========================================================
# MINI PROJECT 2
# NUMBER SUM DIGITS
# ==========================================================

# Find the sum of digits in a number using recursion.

def sum_digits(number):
    if number == 0:
        return 0
    return (number % 10) + sum_digits(number // 10)

num = int(input("Enter a number: "))
digit_sum = sum_digits(abs(num))

print(f"Sum of digits in {num} = {digit_sum}")
