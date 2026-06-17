# Handle multiple conditions efficiently.
# elif checks the next condition only if the previous ones were False

score = 78

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# checking age groups
age = 15

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 60:
    print("You are an adult")
else:
    print("You are a senior")

# day of the week
day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Another day")

# with user input (uncomment to try):
# age = int(input("Enter your age: "))
# if age < 13:
#     print("You are a child")
# elif age < 20:
#     print("You are a teenager")
# else:
#     print("You are an adult")
