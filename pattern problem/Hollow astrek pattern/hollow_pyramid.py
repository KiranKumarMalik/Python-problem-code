#               *
#             *   *       
#           *       *     
#         *           *   
#       * * * * * * * * *

num=int(input("Enter the number of row: "))

for row in range(num):
    for col in range(2*num-1):
        if row+col==num-1 or row==num-1 or col-row==num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()