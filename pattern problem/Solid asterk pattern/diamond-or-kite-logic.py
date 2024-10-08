#                 *
#               * * *
#             * * * * *
#               * * *
#                 *
#
#
#

num = int(input("Enter the number of rows(Odd Number): "))

# Ensure the input is an odd number
spaces = num // 2

# Upper half of the pattern
for row in range(num // 2 + 1):
    # Print leading spaces
    for space in range(spaces):
        print(" ", end=" ")
    # Decrease space count
    spaces-=1
    # Print stars
    for star in range(2 * row + 1):
        print("*", end=" ")
    print()
spaces=1
for row in range(num-2,0,-2):
    for space in range(spaces):
        print(" ", end=" ")
    spaces+=1
    for star in range(row):
        print("*", end=" ")
    print()