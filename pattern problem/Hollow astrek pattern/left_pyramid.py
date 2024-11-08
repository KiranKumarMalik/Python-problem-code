num=int(input("Enter the odd number of row: "))

for row in range(num):
    for col in range(num//2+1):
        if col==0 or row==col or row+col==num-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()