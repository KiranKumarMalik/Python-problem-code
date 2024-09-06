# Inverted left right angled triangle pattern
#  * * * * *
#  * * * * 
#  * * * 
#  * * 
#  * 

n=int(input("Enter the number of row: "))

for i in range(n):  # i is the row number upto n (in range if n=5 then i=0,1,2,3,4 because range is exclusive)
    for j in range(n-i): # i need to print the "*" symbol upto n-i (when i=0 then j=n-i=5)
        print("*", end=" ")
    print()