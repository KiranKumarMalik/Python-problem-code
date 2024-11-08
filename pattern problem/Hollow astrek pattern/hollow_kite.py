# Size of the diamond (half of the diamond's height)
num = int(input("Enter a number of row of half of shape: "))

# Top half of the diamond
for row in range(num):
    # Print leading spaces
    for col in range(num - row - 1):
        print(" ", end=" ")
    # Print stars and spaces in between for the hollow part
    for col in range(2 * row + 1):
        if col == 0 or col == 2 * row:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Bottom half of the diamond
for row in range(num - 2, -1, -1):
    # Print leading spaces
    for col in range(num - row - 1):
        print(" ", end=" ")
    # Print stars and spaces in between for the hollow part
    for col in range(2 * row + 1):
        if col == 0 or col == 2 * row:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
