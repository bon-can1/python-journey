# Repeat actions over a sequence.
# for loop repeats code a fixed number of times or for every  item in a collection

for i in range(1, 6):  # range(start, end, step)
    print(i)

################################################

# factorial 
# 1 x 2 x 3 x 4 x 5 .......

n = int(input("Enter the range: "))
fact = 1
for i in range(1, n+1):
    fact *= i
    print(fact)
print("if you want only last output: ",fact)

###############################################

# fabonaci series
# 0, 1, 1, 2, 3, 5, 8, 13, .....

n = int (input("Enter the range: "))
a = 0
b = 1
for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

#### how it works
# 1 st
# a = 0
# b = 1

# 2nd
# print 0
# c = 0 + 1 -> (a+b) = 1
# a = 1
# b = 1

# 3rd
# print 1
# c = 1 + 2
# a = 1
# b = 2

# 4th 
# print 1
# c = 1 + 2 = 3
# a = 2
# b = 3

# next 2 will print "a"

#################################################################