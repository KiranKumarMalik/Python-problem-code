# To print a diamond pattern using stars
#           *                                                                          *
#         * *           *                                                            * * *
#       * * *           * *                                                        * * * * *
#     * * * *           * * *                                                    * * * * * * *
#   * * * * *     +     * * * *    +               +                =          * * * * * * * * *
#                                        * * * *        * * *                    * * * * * * *
#                                          * * *        * *                        * * * * *
#                                            * *        *                            * * *
#                                              *                                       *
#                                             


n=int(input("Enter the number of rows in first triangle: ")) # number of first right angled triangle rows

for row in range(n):
    for top_left_rightangled_triangle_space in range(n-row-1): # for left triangle number of spaces upto n-row-1 (when row=0 then space=5-0-1=4 spaces)
        print(" ", end=" ")
    for top_left_rightangled_triangle_symbol in range(row+1): # for left triangle number of "*" symbol upto row+1 (when row=0 then symbol=0+1=1)
        print("*", end=" ")
    for top_right_rightangled_triangle_symbol in range(row): # for right triangle number of "*" symbol upto row (when row=0 then symbol=0)
        print("*", end=" ")
    print()
for row in range(n):
    for bottom_left_inverted_right_angled_triangle_space in range(row+1): # for left triangle number of spaces upto row+1 (when row=0 then space=0+1=1 spaces)
        print(" ", end=" ")
    for bottom_left_inverted_right_angled_triangle_symbol in range(n-row-1): # for left triangle number of "*" symbol upto n-row-1 (when row=0 then symbol=5-0-1=4)
        print("*", end=" ")
    for bottom_right_inverted_right_angled_triangle_symbol in range(n-row-2): # for right triangle number of "*" symbol upto n-row-2 (when row=0 then symbol=5-0-2=3)
        print("*", end=" ")
    print()