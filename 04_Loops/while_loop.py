# Repeat while a condition remains true.
# while loop keeps running as long as a condition is True

count = 1

while count <= 5: # condition
    print(count) 
    count += 1 # iteration

####################################################################


password = ""

while password != "python": # here the condition is until the user enter python the loop will not stop
    password = input("Enter password: ")

print("Access Granted")


#####################################################################


# factorial

num = int(input("enter the number: "))
fact = 1
while num > 0:
    fact *= num
    num -= 1
print("factorial =", fact)


#######################################################################


num = int(input("Enter a number that to find how much digit: "))
count = 0

while num > 0:
    num = num //10
    count += 1

print("Digit : ", count)