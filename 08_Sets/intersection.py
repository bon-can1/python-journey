# Find common elements.
# Intersection returns elements present in all given sets
# The intersection operator is &
# The intersection method is intersection()
# Intersection is useful for finding shared items
# Intersection does not modify the original sets


# example 1  intersection using &
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
result = set_a & set_b
print(result)


# example 2  intersection using intersection()
skills_a = {"Python", "Java", "C++"}
skills_b = {"Python", "JavaScript", "Java"}
common = skills_a.intersection(skills_b)
print(common)


# example 3  intersection of three sets
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 6, 7}
result = a & b & c
print(result)


# example 4  no common elements
x = {"apple", "banana"}
y = {"carrot", "potato"}
print(x & y)


# example 5  intersection with strings
group1 = set("python")
group2 = set("program")
print(group1 & group2)


# ==========================================================
# MINI PROJECT 1
# COMMON SUBJECT FINDER
# ==========================================================

# Find subjects common to two students.

student1 = {"Math", "Science", "English", "History"}
student2 = {"Math", "Geography", "English", "Computer"}

common_subjects = student1 & student2

print("Student 1:", student1)
print("Student 2:", student2)
print("Common Subjects:", common_subjects)


# ==========================================================
# MINI PROJECT 2
# SHARED SKILLS CHECKER
# ==========================================================

# Enter skills for two people and show skills both of them have.

person1 = set(
    input("Enter skills for Person 1 (comma separated): ").split(",")
)
person2 = set(
    input("Enter skills for Person 2 (comma separated): ").split(",")
)

shared = person1 & person2

print("\nShared Skills:", shared)

if shared:
    print("Both people know:", ", ".join(shared))
else:
    print("No shared skills found.")
