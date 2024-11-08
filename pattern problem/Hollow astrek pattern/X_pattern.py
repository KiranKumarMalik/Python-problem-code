#                *       *
#                  *   *
#                    *
#                  *   *
#                *       *

num=int(input("Enter the odd number of row: "))

for row in range(num):
    for col in range(num):
        if row+col==num-1 or row==col:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()