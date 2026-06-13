# elif is used to check the condition and if the condition is true then the code will execute otherwise the code will not execute

age = int(input("Enter your age: "))
if age == 20:
    print("you are an adult")
elif age == 10:
    print("you are a child")
else:
    print("you are not born")