#   range(5,6)|         5
#   range(4,6)|       4 5
#   range(3,6)|     3 4 5
#   range(2,6)|   2 3 4 5
#   range(1,6)| 1 2 3 4 5
#

num=int(input("Enter the number of rows: "))
spaces=num-1
for starting_value in range(num,0,-1):
    for space in range(spaces):
        print(" ",end=" ")
    for value in range(starting_value,num+1):
        print(value,end=" ")
    print()
    spaces-=1