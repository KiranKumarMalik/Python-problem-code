#    range(1,2)|         1
#    range(1,3)|       1 2
#    range(1,4)|     1 2 3
#    range(1,5)|   1 2 3 4
#    range(1,6)| 1 2 3 4 5
#

num=int(input("Enter the number of rows: "))
spaces=num-1
for ending_value in range(2,num+2):
    for space in range(spaces):
        print(" ",end=" ")
    for value in range(1,ending_value):
        print(value, end=" ")
    print()
    spaces-=1