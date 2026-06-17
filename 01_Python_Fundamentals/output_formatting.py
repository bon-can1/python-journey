# Display output using f-strings and formatting.

name = "Arun"
age = 20
score = 87.456

# basic print with commas
print("Name:", name, "Age:", age)

# f-string  — put f before the quotes and use { } for variables
print(f"My name is {name} and I am {age} years old")

# expressions inside f-strings
print(f"Next year I will be {age + 1}")

# formatting numbers
print(f"Score: {score}")           # default
print(f"Score: {score:.2f}")       # 2 decimal places
print(f"Score: {score:.0f}")       # no decimal places

# .format() method
print("My name is {} and I am {} years old".format(name, age))

# % formatting (older style, still useful to know)
print("My name is %s and I am %d years old" % (name, age))

# aligning text
print(f"{'Item':<10} {'Price':>8}")
print(f"{'Apple':<10} {'$1.50':>8}")
print(f"{'Banana':<10} {'$0.75':>8}")
