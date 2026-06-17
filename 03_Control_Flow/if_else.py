# Choose between two execution paths.
# if runs when the condition is True, else runs when it is False

age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# checking even or odd
number = 7

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# login example
password = "python123"
entered = "python123"

if entered == password:
    print("Login successful!")
else:
    print("Wrong password. Try again.")

# with user input (uncomment to try):
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are not an adult")
