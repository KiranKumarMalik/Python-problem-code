# Backward right angled trinagle pattern
#        *
#      * *
#    * * *
#  * * * *

num=int(input("Enter the number of row: ")) # n is the number of rows

for row in range(num): # row is the row number upto n (in range if num=5 then row=0,1,2,3,4 because range is esclusive)
    for space in range(num-row):  # space is the number of space upto num-row (when row=0 then space=num-row=4), it will print upto 4 spaces {Logic: Total number of space= total number of row - row number}
        print(" ", end=" ") # Display the space and end=" " is used to print in the same line
    for symbol in range(row+1): # symbol is the number of "*" symbol upto row+1 (when row=0 then symbol=row+1=1)
        print("*", end=" ")  # Display the "*" Symbol and end=" " is used to print in the same line
    print()