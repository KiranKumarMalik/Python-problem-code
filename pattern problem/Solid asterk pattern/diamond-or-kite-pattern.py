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


n=int(input("Enter the number of rows: "))

for i in range(n):
    for top_left_rightangled_triangle_space in range(n-i-1): # for left triangle number of spaces upto n-i-1 (when i=0 then space=5-0-1=4 spaces)
        print(" ", end=" ")
    for top_left_rightangled_triangle_symbol in range(i+1): # for left triangle number of "*" symbol upto i+1 (when i=0 then symbol=0+1=1)
        print("*", end=" ")
    for top_right_rightangled_triangle_symbol in range(i): # for right triangle number of "*" symbol upto i (when i=0 then symbol=0)
        print("*", end=" ")
    print()
for i in range(n):
    for bottom_left_inverted_right_angled_triangle_space in range(i+1): # for left triangle number of spaces upto i+1 (when i=0 then space=0+1=1 spaces)
        print(" ", end=" ")
    for bottom_left_inverted_right_angled_triangle_symbol in range(n-i-1): # for left triangle number of "*" symbol upto n-i-1 (when i=0 then symbol=5-0-1=4)
        print("*", end=" ")
    for bottom_right_inverted_right_angled_triangle_symbol in range(n-i-2): # for right triangle number of "*" symbol upto n-i-2 (when i=0 then symbol=5-0-2=3)
        print("*", end=" ")
    print()