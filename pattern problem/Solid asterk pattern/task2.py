# num=5
#  range(5,6)| 5
#  range(4,6)| 4 5
#  range(3,6)| 3 4 5
#  range(2,6)| 2 3 4 5
#  range(1,6)| 1 2 3 4 5
#  starting_value range(5,0) or range(2,6)
#  
num=int(input("Enter the number of rows: "))
for starting_value in range(num,0,-1):
    for value in range(starting_value,num+1):
        print(value, end=" ")
    print()