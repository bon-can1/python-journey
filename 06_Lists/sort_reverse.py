# Organize and reverse list order
# sort() arranges the elements of a list in ascending order by default
# reverse=True sorts the list in descending order
# reverse() only changes the order of elements; it does NOT sort them
# sorted() returns a NEW sorted list without modifying the original
# sort() only works on lists
# sorted() works on lists, tuples, strings, sets, and more

# experiment 1
a = [10, 50, 30, 70, 20]
a.sort()
print(a)

# experiment 2
a.sort(reverse=True)
print(a)

# experiment 3
b = [10, 50, 30, 70, 20]
b.reverse()
print(b)

# experiment 4 

c = [10, 50, 30, 70, 20]
d = sorted(c)
print(d)

# experiment 5
fruits = ["Mango", "Apple", "Orange", "Banana"]
fruits.sort()
print(fruits)

# experiment 6
fruits.sort(reverse=True)
print(fruits)

# experiment 7
numb = [40, 10, 70, 20]
numb.reverse()
print(numb)

# project 1
# Student Mark ranking
mark = []
n = int(input("How many students: "))
for i in range(n):
    mark.append(int(input("Enter mark: ")))

mark.sort(reverse=True)
print("\nStudent Ranking")
for i, mark in enumerate(mark, start=1):
    print(f"Rank {i}: {mark}")


# project 2
# name organizer
name = []
n = int(input("How many name: "))
for i in range(n):
    name.append(input("Enter name: "))
print("\nAscending Order")
print(sorted(name))
print("\nDescending Order")
print(sorted(name, reverse=True))