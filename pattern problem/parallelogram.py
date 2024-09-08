# To print a parallelogram using pattern
#        * * * * *                    * * * * *
#          * * * *     *                * * * * *
#            * * *     * *                * * * * *
#              * *  +  * * *    =           * * * * *
#                *     * * * *                * * * * *


n=int(input("Enter the number of the rows: "))

for i in range(n):
    for left_triangle_inverted_space in range(i):
        print(" ", end=" ")
    for left_triangle_symbol in range(n-i):
        print("*", end=" ")
    for right_triangle_symbol in range(i):
        print("*", end=" ")
    print()