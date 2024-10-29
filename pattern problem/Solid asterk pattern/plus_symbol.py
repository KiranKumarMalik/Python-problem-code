def plus(size):
    for row in range(size):
        for col in range(size):
            if row==size//2 or col==size//2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

size=int(input("Enter the size of the plus: "))
plus(size)