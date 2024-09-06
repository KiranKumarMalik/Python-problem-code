# Pyramid pattern using loop
#              *
#            * * *
#          * * * * *
#        * * * * * * *
#      * * * * * * * * *


n=int(input("Enter the number of rows: "))

for i in range(n):  # i is the row number upto n (in range if n=5 then i=0,1,2,3,4 because range is exclusive)
    for j in range(n-i-1):  # j is the column number where the space is printed upto n-i-1 (when i=0 then j=n-i-1=5-0-1=4)
        print(" ", end=" ")
    for j in range(i+1):   # j is the column number where the "*" symbol is printed upto i+1 for left right angled triangle (when i=0 then j=i+1=0+1=1)
        print("*", end=" ")
    for j in range(i):  # j is the column number where the "*" symbol is printed upto i for right right angled triangle (when i=0 then j=i=0)
        print("*", end=" ")
    print()