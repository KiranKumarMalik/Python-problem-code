#                 num=5     row   spaces  column  value/num  
#      5 5 5 5 5 5 5 5 5     0       0       9      5   
#        4 4 4 4 4 4 4       1       1       7      4
#         3 3 3 3 3          2       2       5      3       column=2*value-1
#           2 2 2            3       3       3      2
#             1              4       4       1      1
#

num=int(input("Enter the number of rows: "))
col=(2*num)-1
spaces=0
for row in range(num,0,-1):
    for space in range(spaces):
        print(" ", end=" ")
    for value in range(col):
        print(row, end=" ")
    print()
    spaces+=1
    col-=2