# Mirrored right-angled triangle pattern
#      *                 *
#      * *             * *
#      * * *         * * *
#      * * * *     * * * *
#      * * * * * * * * * *

n=int(input("Enter the number of rows: "))

for i in range(1, n+1):
    left_triangle = " ".join("*" * i) # Left triangle with spaces between stars
    right_triangle = " ".join("*" * i) # Right triangle with spaces between stars

# Print left triangle with right alignment and right triangle with spaces between stars
# if n = 5, the widest row in both triangles will have 5 stars and 4 spaces between them, 
# so the total width of the widest triangle is 2 * 5 - 1 = 9
    print(left_triangle.ljust(2 * n - 1) + " " + right_triangle.rjust(2 * n - 1)) #ljust() and rjust() are used to padding alignment