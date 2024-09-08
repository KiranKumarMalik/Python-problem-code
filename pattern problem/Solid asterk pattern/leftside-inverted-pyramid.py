# To print the left sided inverted pyramid pattern
#              *                               *
#              * *                             * *
#              * * *                           * * *
#              * * * *                         * * * *
#              * * * * *    +              =   * * * * *
#                                * * * *       * * * *
#                                * * *         * * *
#                                * *           * *
#                                *             *


n=int(input("Enter the number of rows: "))

for i in range(n):
    for top_right_angled_triangle in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for bottom_right_angled_triangle_symbol in range(n-i-1):
        print("*", end=" ")
    for bottom_right_angled_triangle_space in range(i):
        print(" ", end=" ")
    print()