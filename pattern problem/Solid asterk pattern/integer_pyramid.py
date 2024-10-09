#                           row   spaces  column  value
#             1              0       4       1      1   
#           2 2 2            1       3       3      2
#         3 3 3 3 3          2       2       5      3
#       4 4 4 4 4 4 4        3       1       7      4
#     5 5 5 5 5 5 5 5 5      4       0       9      5
#
num=int(input("Enter the number of rows: "))
col=1
spaces=num-1
for row in range(1,num+1):
    for space in range(spaces):
        print(" ",end=" ")
    for value in range(col):
        print(row, end=" ")
    print()
    spaces-=1
    col+=2

