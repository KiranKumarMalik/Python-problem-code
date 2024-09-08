# To print a parallelogram using pattern
#        * * * * *                    * * * * *
#          * * * *     *                * * * * *
#            * * *     * *                * * * * *
#              * *  +  * * *    =           * * * * *
#                *     * * * *                * * * * *


n=int(input("Enter the number of the rows: "))

for i in range(n):
    for left_triangle_inverted_space in range(i): # space is the number of spaces upto i (when i=0 then space=0)
        print(" ", end=" ")
    for left_triangle_symbol in range(n-i): # symbol is the number of "*" symbol upto n-i (when i=0 then symbol=5-0=5)
        print("*", end=" ")
    for right_triangle_symbol in range(i): # symbol is the number of "*" symbol upto i (when i=0 then symbol=0)
        print("*", end=" ")
    print()