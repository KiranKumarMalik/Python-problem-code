# To print a inverted pyramid
#logic in diagram
#       * * * * *       * * * *         * * * * * * * * *
#         * * * *   +   * * *    =        * * * * * * * 
#           * * *       * *                 * * * * *
#             * *       *                     * * *
#               *                               *


n=int(input("Enter the number of rows: "))

for i in range(n):
    for left_inverted_space in range(i):
        print(" ", end=" ")
    for left_inverted_triangle_symbol in range(n-i):
        print("*", end=" ")
    for right_triangle_symbol in range(n-i-1):
        print("*", end=" ")
    print()