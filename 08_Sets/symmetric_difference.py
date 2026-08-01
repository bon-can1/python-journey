# Find non-overlapping elements.
# Symmetric difference returns elements in either set, but not both
# The symmetric difference operator is ^
# The symmetric difference method is symmetric_difference()
# It removes common elements and keeps unique ones from both sides
# Symmetric difference is useful for comparing two groups


# example 1  symmetric difference using ^
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
result = set_a ^ set_b
print(result)


# example 2  symmetric difference using method
team_a = {"Arun", "Priya", "Ravi"}
team_b = {"Priya", "Kiran", "Meera"}
unique = team_a.symmetric_difference(team_b)
print(unique)


# example 3  no overlap
x = {"apple", "banana"}
y = {"carrot", "potato"}
print(x ^ y)


# example 4  identical sets
a = {1, 2, 3}
b = {1, 2, 3}
print(a ^ b)


# example 5  compare two wishlists
wishlist1 = {"Book", "Headphones", "Shoes"}
wishlist2 = {"Book", "Watch", "Bag"}
different = wishlist1 ^ wishlist2
print(different)


# ==========================================================
# MINI PROJECT 1
# UNIQUE PREFERENCES
# ==========================================================

# Find food items liked by only one person, not both.

person_a = {"Pizza", "Burger", "Pasta", "Salad"}
person_b = {"Pizza", "Sushi", "Salad", "Tacos"}

unique_tastes = person_a ^ person_b

print("Person A:", person_a)
print("Person B:", person_b)
print("Unique to Each Person:", unique_tastes)


# ==========================================================
# MINI PROJECT 2
# MOVIE DIFFERENCE CHECKER
# ==========================================================

# Compare movies watched by two friends and show movies only one of them watched.

friend1 = set(
    input("Enter movies watched by Friend 1 (comma separated): ").split(",")
)
friend2 = set(
    input("Enter movies watched by Friend 2 (comma separated): ").split(",")
)

only_one_watched = friend1 ^ friend2

print("\nMovies watched by only one friend:")
print(only_one_watched)
