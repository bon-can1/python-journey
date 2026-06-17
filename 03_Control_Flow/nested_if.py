# Place conditions inside conditions.
# nested if means an if block inside another if block

age = 22
has_id = True

if age >= 18:
    print("Age check passed.")
    if has_id:
        print("You can enter the club.")
    else:
        print("You need an ID to enter.")
else:
    print("You are too young to enter.")

# another example — checking number range and sign
number = 15

if number > 0:
    print("The number is positive.")
    if number % 2 == 0:
        print("It is also even.")
    else:
        print("It is also odd.")
else:
    print("The number is zero or negative.")

# exam result with bonus
score = 85
attended = True

if attended:
    if score >= 90:
        print("Excellent! You get a certificate.")
    elif score >= 50:
        print("You passed the exam.")
    else:
        print("You failed. Study harder.")
else:
    print("You were absent. Cannot evaluate.")
