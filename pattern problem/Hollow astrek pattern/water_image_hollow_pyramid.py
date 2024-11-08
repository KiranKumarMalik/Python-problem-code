#            * * * * * * * * *
#              *           *
#                *       *
#                  *   *
#                    *

num=int(input("Enter the number of row: "))

for row in range(num):
    for col in range(2*num-1):
        if row==0 or row==col or row+col==(num-1)*2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()