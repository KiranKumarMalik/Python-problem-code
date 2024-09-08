# Write a program to print right side inverted pyramid pattern
#                      *                                 *
#                    * *                               * *
#                  * * *                             * * *
#                * * * *                           * * * *
#              * * * * *                         * * * * *
#                         +   * * * *    =         * * * *
#                               * * *                * * *
#                                 * *                  * *
#                                   *                    *
n=int(input("Enter the number of rows: "))

for i in range(n):
    for top_right_angled_triangle_space in range(n-i-1): # space is the number of spaces upto n-i-1 (when i=0 then space= 5-0-1=4 spaces)
        print(" ", end=" ")
    for top_right_angled_triangle_symbol in range(i+1): # symbol is the number of "*" symbol upto i+1 (when i=0 then symbol=0+1=1)
        print("*", end=" ")
    print()
for i in range(n):
    for bottom_right_angled_triangle_space in range(i+1): # space is the number of spaces upto i+1 (when i=0 then space=0+1=1 spaces)
        print(" ", end=" ")
    for bottom_right_angled_triangle_symbol in range(n-i-1): # symbol is the number of "*" symbol upto n-i-1 (when i=0 then symbol=5-0-1=4)
        print("*", end=" ")
    print()