# Exit a loop early.
# The break statement is used to immediately stop a loop, 
#       even if the loop condition is still True.

for i in range(1, 11):

    if i == 5:
        break  # here the loop run till 1 to 10 but due to this break statement it will stop at 4

    print(i)


##############################################################


password = ""
count = 0
while password != "admin":
    password = input("enter password: ")
    if password == "admin":
        print("Successfull")
    else:
        print("Wrong password")
        print(f"Your attempt: {count}")

    count += 1
    if count == 3:
        print("login failed")
        break
