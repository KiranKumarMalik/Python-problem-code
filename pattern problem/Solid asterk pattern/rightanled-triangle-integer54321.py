# num=5
#  range(1,0,-1)| 1
#  range(2,0,-1)| 2 1
#  range(3,0,-1)| 3 2 1
#  range(4,0,-1)| 4 3 2 1
#  range(5,0,-1)| 5 4 3 2 1
#  ending_value range(1,5+1)
#  
num=int(input("Enter the number of rows: "))
for starting_value in range(1,num+1):
    for value in range(starting_value,0,-1):
        print(value, end=" ")
    print()