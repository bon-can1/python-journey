# Find unique elements.
# Difference returns elements in the first set but not in the second
# The difference operator is -
# The difference method is difference()
# Order matters in difference operations
# Difference is useful for finding what is missing or extra


# example 1  difference using -
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
result = set_a - set_b
print(result)


# example 2  difference using difference()
all_skills = {"Python", "Java", "C++", "HTML"}
known_skills = {"Python", "HTML"}
remaining = all_skills.difference(known_skills)
print(remaining)


# example 3  reverse difference
a = {10, 20, 30}
b = {20, 30, 40}
print(a - b)
print(b - a)


# example 4  difference with no unique values
x = {"apple", "banana"}
y = {"apple", "banana", "mango"}
print(x - y)


# example 5  remove installed apps from required list
required = {"Python", "Git", "VS Code", "Docker"}
installed = {"Python", "Git"}
missing = required - installed
print("Missing:", missing)


# ==========================================================
# MINI PROJECT 1
# MISSING ITEM FINDER
# ==========================================================

# Find items required for a trip but not yet packed.

required_items = {
    "Passport",
    "Ticket",
    "Clothes",
    "Shoes",
    "Charger"
}

packed_items = {
    "Clothes",
    "Shoes",
    "Charger"
}

missing_items = required_items - packed_items

print("Required:", required_items)
print("Packed:", packed_items)
print("Still Missing:", missing_items)


# ==========================================================
# MINI PROJECT 2
# SKILLS TO LEARN
# ==========================================================

# Compare target skills with current skills and show what is left to learn.

target = set(
    input("Enter target skills (comma separated): ").split(",")
)
current = set(
    input("Enter current skills (comma separated): ").split(",")
)

to_learn = target - current

print("\nSkills Left to Learn:", to_learn)

if to_learn:
    print("You still need to learn:", ", ".join(to_learn))
else:
    print("You already know all target skills!")
