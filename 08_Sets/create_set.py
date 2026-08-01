# Store unique values only.
# A set is a collection of unique elements
# Sets are unordered
# Sets do not allow duplicate values
# Sets are mutable (we can add and remove items)
# Sets use curly braces {} or the set() function
# Sets are useful for removing duplicates and membership testing


# example 1  basic set
numbers = {1, 2, 3, 4, 5}
print(numbers)


# example 2  duplicate values removed automatically
colors = {"red", "blue", "red", "green", "blue"}
print(colors)


# example 3  mixed data types
data = {"Python", 100, True}
print(data)


# example 4  empty set
# Use set() because {} creates an empty dictionary
empty = set()
print(empty)
print(type(empty))


# example 5  create set from list
fruits = set(["apple", "banana", "apple", "mango"])
print(fruits)


# example 6  create set from string
letters = set("hello")
print(letters)


# ==========================================================
# MINI PROJECT 1
# DUPLICATE REMOVER
# ==========================================================

# Take words from the user and store only unique words in a set.

words = set()
n = int(input("How many words: "))

for i in range(n):
    word = input("Enter word: ")
    words.add(word)

print("\nUnique Words")
print(words)


# ==========================================================
# MINI PROJECT 2
# UNIQUE EMAIL COLLECTOR
# ==========================================================

# Collect email addresses and show only unique emails.

emails = set()
count = int(input("How many emails: "))

for i in range(count):
    email = input("Enter email: ")
    emails.add(email)

print("\nUnique Email List")
for email in emails:
    print(email)
