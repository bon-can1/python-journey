# Combine multiple sets.
# Union combines all unique elements from two or more sets
# Duplicate values appear only once
# The union operator is |
# The union method is union()
# Union is useful when merging collections
# Union does not modify the original sets


# example 1  union using |
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a | set_b
print(result)


# example 2  union using union()
fruits = {"apple", "banana"}
vegetables = {"carrot", "potato"}
all_items = fruits.union(vegetables)
print(all_items)


# example 3  union with duplicates
a = {"Python", "Java", "C++"}
b = {"Java", "JavaScript", "Go"}
c = a | b
print(c)


# example 4  union of three sets
x = {1, 2}
y = {2, 3}
z = {3, 4}
combined = x | y | z
print(combined)


# example 5  update using union
team_a = {"Arun", "Priya"}
team_b = {"Ravi", "Kiran"}
team_a.update(team_b)
print(team_a)


# ==========================================================
# MINI PROJECT 1
# CLASS MERGER
# ==========================================================

# Merge students from two classes and show the full unique list.

class_a = {"Arun", "Priya", "Ravi"}
class_b = {"Kiran", "Priya", "Meera"}

all_students = class_a | class_b

print("Class A:", class_a)
print("Class B:", class_b)
print("All Students:", all_students)
print("Total Students:", len(all_students))


# ==========================================================
# MINI PROJECT 2
# HOBBY COMBINER
# ==========================================================

# Combine hobbies of two friends and display unique hobbies.

friend1 = set(
    input("Enter hobbies for Friend 1 (comma separated): ").split(",")
)
friend2 = set(
    input("Enter hobbies for Friend 2 (comma separated): ").split(",")
)

common_hobbies = friend1 | friend2

print("\nFriend 1 Hobbies:", friend1)
print("Friend 2 Hobbies:", friend2)
print("Combined Unique Hobbies:", common_hobbies)
