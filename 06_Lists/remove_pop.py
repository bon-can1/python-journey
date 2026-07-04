# Remove elements from lists.
# remove(), pop(), clear(), del?
# -> remove() the first matching value
# -> pop () removes an element using it's index or 
#       if no index is given, it removes the last element
# -> clear() remove all elements from the list
# -> del Deletes an element, multiple elements, or the entire list


# example 1   remove()

fruit = ["Apple", "Banana", "Orange"]
fruit.remove("Banana")
print(fruit)


# example 2   remove() with Duplicate Values

num = [10, 20, 30 ,40]
num.remove(20)
print(num)


# example 3   pop()
color = ["Red", "Green", "Blue"]
color.pop(1)
print(color)


# example 4   pop() without index
color = ["Red", "Green", "Blue"]
color.pop()
print(color)


# example 5   clear()
color = ["Red", "Green", "Blue"]
color.clear()
print(color)


# example 6   del
color = ["Red", "Green", "Blue"]
del color[1]
print(color)


# example 7   delete entire list
animals = ["Dog","Cat","Lion"]
del animals


# PROJECT 1
# To-Do List Manager

tasks = []

while True:

    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Choice : ")

    if choice == "1":
        task = input("Task : ")
        tasks.append(task)
    elif choice == "2":
        task = input("Task to Remove : ")
        if task in tasks:
            tasks.remove(task)
            print("Task Removed")
        else:

            print("Task Not Found")
    elif choice == "3":
        print("\nTasks")
        for task in tasks:
            print("-", task)
    elif choice == "4":
        break
