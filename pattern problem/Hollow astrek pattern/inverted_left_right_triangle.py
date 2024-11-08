#            * * * * *
#              *     *
#                *   *
#                  * *
#                    *

num=int(input("Enter the number of row: "))

for row in range(num):
    for col in range(num):
        if row==col or row==0 or col==num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()