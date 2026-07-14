# Loop through list elements.
# Iteration means visiting each element of list one by one
# A for loop is the most common way to iterate through a list
# We can access indexes using range() and len()
# enumerate() gives both the index and value
# while loops can also be used for list iteration

# example 1  basic for loop 
fruit = ['Apple', 'Banana', 'Mango']
for fruit in fruit:
    print(fruit)


# example 2  iteration through number
num = [10, 20, 30, 40]
for n in num:
    print(num)


# example 3  performing calculation
num = [1, 2, 3, 4, 5]
for n in num:
    print(n * n)


# example 4  using range() and len()
lag = ['Python', 'Java', 'C++']
for i in range(len(lag)):
    print(i, lag[i])


# example 5 using enumerate()
stu = ['Arun', 'Boban', 'iya']
for index, student in enumerate(stu):
    print(index, student)


# example 6  while loop iteration
color = ['red', 'blue', 'Green']
i = 0
while i < len(color):
    print(color[i])
    i += 1


# example 7  filitering while iteration 
matr = [90, 35, 75, 20, 88]
for m in matr:
    if m < 40:
        continue
    print("Password: ", m)


# example 8  calculate total
price = [100, 250, 50, 300]
total = 0
for p in price:
    total += p
print("total: ", total)


# example 9  nested list iteration
stu =[
    ["Arun", 90],
    ["Iya", 80],
    ["jo", 85]
]
for st in stu:
    print("name: ", stu[0])
    print("Mark: ", stu[1])


# example 10  nested loops with list

mat = [
    [1, 2],
    [3, 4],
    [5, 6]
]
for r in mat:
    for n in r:
        print(n, end=' ')
    print()


########################################################################################
# MINI PROJECT 1
# SHOPPING BILL CALCULATOR


prices = []

n = int(input("How many products? "))

for i in range(n):
    price = float(input("Enter product price: "))
    prices.append(price)

total = 0

for price in prices:
    total += price

print("\nProduct Prices")

for index, price in enumerate(prices, start=1):
    print(f"{index}. ${price}")

print("Total Bill: $", total)

####################################################################################
# mini project 2  student result system


mark = []
n = int(input("\nHow many Student? "))
for i in range(n):
    m = int(input("Enter mark: "))
    mark.append(m)

print("\nStudent Result")
for ind , mark in enumerate(mark, start=1):
    if mark >= 40:
        result = "pass"
    else:
        result = "Fail"
    print(f"student {ind}: {mark} = {result}")