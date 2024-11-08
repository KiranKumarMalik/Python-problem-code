num=int(input("Enter the odd number of row of half kite: "))

for row in range(num):
    for col in range(num):
        if row-col==num//2 or row+col==num//2 or col-row==num//2 or row+col==(num//2)*3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()