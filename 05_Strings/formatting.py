# Format strings for readable output.
# Formatting helps you display text cleanly with variables and numbers.
# Main methods: f-strings (best), .format(), and % formatting.

name = "Arun"
age = 20
score = 87.456

# f-string — put f before quotes and use {variable}
print(f"My name is {name} and I am {age} years old")

# expressions inside f-strings
print(f"Next year I will be {age + 1}")

# number formatting
print(f"Score: {score:.2f}")      # 2 decimal places if you want to increse the decimal then change the 2
print(f"Score: {score:.0f}")      # no decimals
print(f"Percentage: {score:.1f}%")

# .format() method
print("Hello {}, you are {} years old".format(name, age))       # each Curly brackets inside the double cots can given by var  
print("Hello {n}, you are {a} years old".format(n=name, a=age)) # here we give a simple small shot var for the big name

# % formatting (older style)
print("Hello %s, you are %d years old" % (name, age))  # this was the older way to make the output "%s" -> string, "%d" -> digit. In few language like c, c++, ... we are still using this methods

# aligning text in columns
print(f"{'Item':<12} {'Price':>8}")   # for proper gap with the text 
print(f"{'Apple':<12} {'$1.50':>8}")
print(f"{'Banana':<12} {'$0.75':>8}")

# padding numbers
num = 7
print(f"Number with zeros: {num:03d}")   # 007

############################################################

# Student Report Card


student = input("Enter student name: ")
math = float(input("Enter math score: "))
science = float(input("Enter science score: "))
english = float(input("Enter english score: "))

average = (math + science + english) / 3

print("\n--- REPORT CARD ---")
print(f"Student : {student}")
print(f"Math    : {math:.1f}")
print(f"Science : {science:.1f}")
print(f"English : {english:.1f}")
print(f"Average : {average:.2f}")

if average >= 50:
    print("Result  : PASS")
else:
    print("Result  : FAIL")

############################################################

# Shopping Bill Formatter
# Create a neat bill with aligned columns.

print("\n--- SHOPPING BILL ---")
print(f"{'Item':<15} {'Qty':>5} {'Price':>8} {'Total':>8}")
print("-" * 40)

items = [
    ("Apple", 3, 1.50),
    ("Bread", 1, 2.00),
    ("Milk", 2, 1.25),
]

grand_total = 0
for item, qty, price in items:
    total = qty * price
    grand_total += total
    print(f"{item:<15} {qty:>5} {price:>8.2f} {total:>8.2f}")

print("-" * 40)
print(f"{'Grand Total':<15} {'':>5} {'':>8} {grand_total:>8.2f}")
