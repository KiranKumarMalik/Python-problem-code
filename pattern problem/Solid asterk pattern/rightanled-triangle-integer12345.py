# num=5
#  range(1,2)| 1
#  range(1,3)| 1 2
#  range(1,4)| 1 2 3
#  range(1,5)| 1 2 3 4
#  range(1,6)| 1 2 3 4 5
#  ending_value range(2,5+2) or range(2,7)
#    
num=int(input("Enter the number of rows: "))
for ending_value in range(2,num+2):
    for value in range(1,ending_value):
        print(value, end=" ")
    print()