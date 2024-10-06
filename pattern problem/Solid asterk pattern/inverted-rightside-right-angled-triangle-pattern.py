# Inverted left right angled triangle pattern
#   * * * * * 
#     * * * * 
#       * * * 
#         * * 
#           * 

num=int(input("Enter the number of rows: "))

for row in range(num):  # row is the row number upto n (in range if n=5 then row=0,1,2,3,4 because range is exclusive)
    for space in range(row): # space is the number of space upto row (when row=0 then space=0)
        print(" ", end=" ") # Display the space and end=" " is used to print in the same line
    for symbol in range(num-row): # symbol is the number of "*" symbol upto num-row (when row=0 then symbol: 5-0=5)
        print("*", end=" ")
    print()