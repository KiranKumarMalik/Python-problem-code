# num=5
#  range(5,4,-1)| 5
#  range(5,3,-1)| 5 4
#  range(5,2,-1)| 5 4 3
#  range(5,1,-1)| 5 4 3 2
#  range(5,0,-1)| 5 4 3 2 1
#  starting_value range(5,0) or range(2,6)
#  
num=int(input("Enter the number of rows: "))
for ending_value in range(num,0,-1):
    for value in range(num,ending_value-1,-1):
        print(value, end=" ")
    print()