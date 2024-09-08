# Mirrored right-angled triangle pattern
#      *                 *
#      * *             * *
#      * * *         * * *
#      * * * *     * * * *
#      * * * * * * * * * *

n=int(input("Enter the number of rows: "))

for i in range(n): # i is the row number upto n (in range if n=5 then i=0,1,2,3,4 because range is exclusive)
    for left_column_symbol in range (i+1): # j is the column number upto i+1(when i=0 then j=i+1 column=1)
        print("*", end=" ") 
    for inverted_left_triangle__space in range(n-i-1): # inverted_left_triangle_space is the number of space of inverted left triangle
        print(" ", end=" ")
    for inverted_right_triangle_space in range(n-i-1): # inverted_right_triangle_space is the number of space of inverted right triangle
        print(" ", end=" ")
    for right_column_symbol in range(i+1):
        print("*", end=" ")
    print()