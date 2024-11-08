#            * * * * *
#                *
#                *
#                *
#                *

num=int(input("Enter the odd number of row: "))

for row in range(num):
    for col in range(num):
        if row==0 or col==num//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()