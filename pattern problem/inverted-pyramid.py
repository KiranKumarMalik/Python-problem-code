# To print a inverted pyramid
#logic in diagram
#       * * * * *       * * * *         * * * * * * * * *
#         * * * *   +   * * *    =        * * * * * * * 
#           * * *       * *                 * * * * *
#             * *       *                     * * *
#               *                               *


n=int(input("Enter the number of rows: "))

for i in range(n):
    for left_inverted_space in range(i): # space is the number of spaces upto i (when i=0 then space=0)
        print(" ", end=" ")
    for left_inverted_triangle_symbol in range(n-i): # symbol is the number of "*" symbol upto n-i (when i=0 then symbol=5-0=5)
        print("*", end=" ")
    for right_triangle_symbol in range(n-i-1): # symbol is the number of "*" symbol upto n-i-1 (when i=0 then symbol=5-0-1=4)
        print("*", end=" ")
    print()