
#            1
#          2 2
#        3 3 3
#      4 4 4 4 
#    5 5 5 5 5

num=int(input("Enter the number of rows: "))
for row in range(1,num+1):
    for space in range(num-row):
        print(" ", end=" ")
    for symbol in range(row):
        print(row, end=" ")
    print()