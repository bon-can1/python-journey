# Create and store collections of data.
# A list is a collection of multiple item stored in a single variable
# Lists are mutable, meaning we can add, remove or modify items
# lists allow duplicate values
# lists can store different data type together
# list can store different data type together
# Lists are one of the most commonly used data structures in Python


shopping_cart = ["Milk", "Bread", "Eggs", "Butter"]
print(shopping_cart)

# Imagine your shopping cart.

# Milk
# Bread
# Eggs
# Butter

# Instead of creating

# milk = "Milk"
# bread = "Bread"
# eggs = "Eggs"

# here we store all together

#############################################################
# example 1  Integer list
num = [10, 20, 30, 40]
print(num)


# example 2  String list
lang = ["Python", "Java", "C++", "JavaScript"]
print(lang)


# example 3  Mixed data types
stu = ["Arun", 20, 7.8, True]
print(stu)


# example 4  Empty list
task = []
print(task)


# example 5  Duplicate value
color = ["red", "blue", "red", "green"]
print(color)


# example 6  Nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)


# example 7  create list using list()
numb = list((1, 2, 3, 4, 5))
print(numb)


########################################################################

# Project 1
# how many students? store all name in a list. print the complete list.
stud = []
n = int(input("how many students: "))
for i in range(n):
    name = input("enter the name: ")
    stud.append(name)  # append is used to add item to a list from last
print("\n registered student")
print(stud)
