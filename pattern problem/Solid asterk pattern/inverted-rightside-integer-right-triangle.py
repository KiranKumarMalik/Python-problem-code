#       5 5 5 5 5
#         4 4 4 4
#           3 3 3
#             2 2
#               1

num=int(input("Enter the number of row: ")) 
for row in range(num,0,-1):
    for space in range(num-row):
        print(" ", end=" ")
    for col in range(row):
        print(row, end=' ')
    print()