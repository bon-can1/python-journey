# A nested loop is simply a loop inside another loop.


for i in range(3):

    for j in range(3):

        print(i, j) # here you see the 4th line loop run 1st there 3 times 
                    #     2nd loop and the 4th line loop run repeat the process

############################################################

# Let's build Mini Project 1: Star Pattern step by step.


n = int(input("enter the number of row you want: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()


############################################################
# multiplication Table
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()