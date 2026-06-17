# Combine conditions using and, or, not.
# logical operators return True or False

age = 20
has_ticket = True
is_weekend = False

# and — both conditions must be True
print("age >= 18 and has_ticket:", age >= 18 and has_ticket)   # True
print("age >= 18 and is_weekend:", age >= 18 and is_weekend)   # False

# or — at least one condition must be True
print("has_ticket or is_weekend:", has_ticket or is_weekend)   # True
print("age < 10 or is_weekend:", age < 10 or is_weekend)       # False

# not — reverses True to False and False to True
print("not has_ticket:", not has_ticket)   # False
print("not is_weekend:", not is_weekend)   # True

# combining all three
score = 85
passed = score >= 50 and score <= 100
print("Passed exam:", passed)

# real-world style check
if age >= 18 and has_ticket:
    print("You can enter the event")
else:
    print("You cannot enter the event")
