num=int(input("Enter the odd number of row of half kite: "))

for row in range(num):
    for col in range(num//2+1):
        if col==num//2 or row+col==num//2 or row-col==num//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()