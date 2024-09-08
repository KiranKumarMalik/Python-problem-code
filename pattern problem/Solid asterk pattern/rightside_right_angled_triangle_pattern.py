# Backward right angled trinagle pattern
#        *
#      * *
#    * * *
#  * * * *

n=int(input("Enter the number of row: ")) # n is the number of rows

for i in range(n): # i is the row number upto n (in range if n=5 then i=0,1,2,3,4 because range is esclusive)
    for space in range(n-i-1):  # space is the number of space upto n-i (when i=0 then space=n-i-1=4), it will print upto 4 spaces {Logic: Total number of space= total number of row - row number}
        print(" ", end=" ") # Display the space and end=" " is used to print in the same line
    for symbol in range(i+1): # symbol is the number of "*" symbol upto i+1 (when i=0 then symbol=i+1=1)
        print("*", end=" ")  # Display the "*" Symbol and end=" " is used to print in the same line
    print()