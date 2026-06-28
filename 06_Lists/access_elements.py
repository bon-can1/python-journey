# Access list items using indexes.
#  Accessing means retrieving an item from a list
#  Every element has a position called an Index
#  Python indexing always starts from 0
#  Negative indexing starts from the end
#  We can also access multiple elements using slicing
#  Accessing data is one of the most common list operations

#######################################################################

# example 1  positive indexing  (start from 0)

fruits = ["Apple", "Orange", "Banana", "Mango"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

# example 2 negative indexing  (start from -1)
# -1 means last element, -2 second last, -3 third last

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])


# example 3   accessing user information
user = [
    "Arun",
    20,
    "India",
    "Python Developer"
]
print("Name: ", user[0])
print("Age: ", user[1])
print("Country : ", user[2])
print("Role : ", user[3])


# example 4  Accessing Nested lists

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0])
print(matrix[1])
print(matrix[2])

# example 5  access specific value in nested list

print(matrix[0][0])
print(matrix[1][2])
print(matrix[2][1])


# example 6  Slicing

num = [10, 20 ,30, 40, 50, 60]
print(num[1:4])
print(num[:3])
print(num[3:])


# example 7  Skip elements

print(num[::2])  # print in the order of 0 2 4 6
print(num[::-1]) # print from last to start


##########################################################################

# project 1
# Student search

stu = [] # empty list
n = int(input("Enter how many students: "))
for i in range(n):
    stu.append(input("Enter student name: "))
ind = int(input(f"enter index (0 to {len(stu)-1}) to search the student name: "))
if 0 <= ind < len(stu):
    print("Student: ", stu[ind])
else: 
    print("Invaild index")

