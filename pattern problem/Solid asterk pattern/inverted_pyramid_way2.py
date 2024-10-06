# Inverted left right angled triangle pattern
#  * * * * *
#  * * * * 
#  * * * 
#  * * 
#  * 

num=int(input("Enter the number of rows: "))
for row in range(num):
    for space in range(row):
        print(" ", end=" ")
    for symbol in range(2*(num-row)-1):
        print("*", end=" ")
    print()