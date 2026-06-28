# Add new elements to lists
# append() adds ONE element at the END of a list
# insert() adds an element at a SPECIFIC POSITION
# append() always increases the list size by one
# insert() shifts existing elements to the right
# Both methods modify the original list
# append() is faster than insert() in most cases

# example 1   append()
from tkinter import N


fruit = ["apple", "banana"]
fruit.append("Orange")
print(fruit)


# example 2   append multiple times
num = []
num.append(10)
num.append(20)
num.append(30)
print(num)


# example 3   insert
stud = ["Arun", "Hevin"]
stud.insert(1, "MJ")
print(stud)


# example 4   insert at beginning
lag = ["Java", "C", "C++"]
lag.insert(0, "Python")
print(lag)


# example 5  insert at end
num = [1, 2, 3, 4]
num.insert(len(num), 5)
print(num)


# example 5 append a list 
numb = [1, 2, 3, 4]
numb.append([5, 6])  # it will add like a list
print(numb)


# example 6  extend 
n = [1, 2, 3]
n.extend([4, 5, 6])  # it will add element by element
print(n)


####################################################################

# project 1
# Student Admission System
stud = []
n = int(input("How many students: "))
for i in range(n):
    name = input("enter the name: ")
    stud.append(name)
print("Students")
for st in stud:
    print(st)


###################################################################


# project 2
# Priority Task Manager

task = []
while True:
    print("\n1. add normal task")
    print("2. add priority task")
    print("3. add show task")
    print("4. Exit")

    choice = int(input("Enter you Choice number: "))
    if choice == 1:
        t = input("Task: ")
        task.append(t)
    elif choice == 2:
        t = input("enther the priority task: ")
        task.insert(0, t)
    elif choice == 3:
        print("task: ")
        for t in task:
            print(t)
    else:
        break
print("thank you using task manager")