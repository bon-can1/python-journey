# Modify set contents.
# Sets are mutable, so items can be added and removed
# add() inserts a single element
# update() adds multiple elements at once
# remove() deletes an element and raises error if missing
# discard() deletes an element safely without error
# pop() removes and returns a random element
# clear() removes all elements from the set


# example 1  add single element
skills = {"Python", "Java"}
skills.add("C++")
print(skills)


# example 2  update multiple elements
skills.update(["HTML", "CSS", "JavaScript"])
print(skills)


# example 3  remove element
skills.remove("Java")
print(skills)


# example 4  discard element safely
skills.discard("Ruby")
print(skills)


# example 5  pop random element
removed = skills.pop()
print("Removed:", removed)
print(skills)


# example 6  clear set
backup = skills.copy()
skills.clear()
print(skills)


# ==========================================================
# MINI PROJECT 1
# SHOPPING LIST MANAGER
# ==========================================================

# Add items to a shopping set and remove one item when done.

cart = set()

print("Add items to cart (type 'done' to stop)")

while True:
    item = input("Enter item: ")

    if item.lower() == "done":
        break

    cart.add(item)

print("\nCurrent Cart")
print(cart)

remove_item = input("Enter item to remove: ")
cart.discard(remove_item)

print("\nUpdated Cart")
print(cart)


# ==========================================================
# MINI PROJECT 2
# SKILL TRACKER
# ==========================================================

# Start with some skills, add new ones, and remove an old skill.

skills = {"Python", "HTML", "CSS"}

print("Current Skills:", skills)

new_skill = input("Enter a new skill to add: ")
skills.add(new_skill)

old_skill = input("Enter a skill to remove: ")
skills.discard(old_skill)

print("\nUpdated Skills")
print(skills)
