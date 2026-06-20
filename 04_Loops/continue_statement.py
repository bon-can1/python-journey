# Skip the current iteration.
# The continue statement is used to skip the current iteration and move directly 
#       to the next iteration of the loop.

for i in range(1, 6):

    if i == 3:
        continue # here the loop run till 5 with no gap but, due to "countinue statement" there is not 3 it will skip

    print(i)

# defferents between break and continue is stop and skip a step

############################################################


# print even number
n = int(input("Enter the range: "))
for i in range(0, n):
    if i % 2 != 0:
        continue
    else:
        print(i, end=" ")