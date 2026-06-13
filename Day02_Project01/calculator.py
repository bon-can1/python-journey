# here we are going to make a calculator that can add, subtract, multiply, divide and modulus

import math
choice = int(input("Enter your choice (how number you input 1 or 2): "))
if(choice == 1):  # if condition the check the your choice
    num1 = int(input("Enter the first number: "))
    cha = input("Enter the arithematic oparetion (square, root, abs): ")
    if(cha == "root"):
        print("result: ", round(math.sqrt(num1), 2))
    elif(cha == "abs"):
        print("result: ", abs(num1))
    elif(cha == "square"):
        print("result: ", round(math.pow(num1, 2), 2))
    else:
        print("not mention a number!\n")


elif(choice == 2):
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    cha = input("Enter the arithematic oparetion (+, -, /, *, //, **, %): ")
    if(cha == "+"):
        print("result: ", num1 + num2)
    elif(cha == "-"):
        print("result: ", num1 - num2)
    elif(cha == "*"):
        print("result: ", num1 * num2)
    elif(cha == "/"):
        print("result: ", num1 / num2)
    elif(cha == "//"):
        print("result: ", num1 // num2)
    elif(cha == "**"):
        print("result: ", num1 ** num2)
    else:
        print("the number is not mention")

else:
    print("the number is not mention")