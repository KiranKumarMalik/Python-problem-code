#   range(5,4,-1)|         5
#   range(5,3,-1)|       5 4
#   range(5,2,-1)|     5 4 3
#   range(5,1,-1)|   5 4 3 2
#   range(5,0,-1)| 5 4 3 2 1
#

num=int(input("Enter the number of rows: "))
spaces=num-1
for ending_value in range(num-1,-1,-1):
    for space in range(spaces):
        print(" ", end=" ")
    for value in range(num,ending_value,-1):
        print(value,end=" ")
    print()
    spaces-=1