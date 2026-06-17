# Accept input from users during execution.
# input() pauses the program and waits for the user to type something

name = input("Enter your name: ")  # always returns a string
print("Hello,", name)

age = input("Enter your age: ")
print("You entered:", age, "Type:", type(age))

# convert input to other types when needed
age_number = int(input("Enter your age as a number: "))
print("Next year you will be", age_number + 1)

height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters")

favorite = input("What is your favorite language? ")
print(f"Nice! {favorite} is a great choice.")
