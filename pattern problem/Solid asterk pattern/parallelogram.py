# To print a parallelogram using pattern
#        * * * * *                    * * * * *
#          * * * *     *                * * * * *
#            * * *     * *                * * * * *
#              * *  +  * * *    =           * * * * *
#                *     * * * *                * * * * *


num=int(input("Enter the number of the rows: "))

for row in range(num):
    for left_triangle_inverted_space in range(row): # space is the number of spaces upto row (when row=0 then space=0)
        print(" ", end=" ")
    for left_triangle_symbol in range(num-row): # symbol is the number of "*" symbol upto num-row (when row=0 then symbol=5-0=5)
        print("*", end=" ")
    for right_triangle_symbol in range(row): # symbol is the number of "*" symbol upto row (when row=0 then symbol=0)
        print("*", end=" ")
    print()
    