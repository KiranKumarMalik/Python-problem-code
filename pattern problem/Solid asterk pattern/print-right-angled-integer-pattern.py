#      1
#      2 2
#      3 3 3
#      4 4 4 4
#      5 5 5 5 5

num=4
for row in range(1,num+1):
    for col in range(row):
        print(row, end=" ")
    print()