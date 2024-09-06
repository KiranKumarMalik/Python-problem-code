# Inverted left right angled triangle pattern
#   * * * * * 
#     * * * * 
#       * * * 
#         * * 
#           * 

n=int(input("Enter the number of rows: "))

for i in range(n):  # i is the row number upto n (in range if n=5 then i=0,1,2,3,4 because range is exclusive)
    for space in range(i): # space is the number of space upto i (when i=0 then space=0)
        print(" ", end=" ") # Display the space and end=" " is used to print in the same line
    for symbol in range(n-i): # symbol is the number of "*" symbol upto n-i (when i=0 then symbol: 5-0=5)
        print("*", end=" ")
    print()