#            * * * * * 
#            *     *   
#            *   *     
#            * *       
#            *

num=int(input("Enter the number of row: "))

for row in range(num):
    for col in range(num):
        if row==0 or col==0 or row+col==num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()