# Backward right angled trinagle pattern
#        *
#      * *
#    * * *
#  * * * *

num=int(input("Enter the number of rows: "))
for row in range(1,num+1):
    for space in range(num-row):
        print(" ", end=" ")
    for symbol in range(row):
        print("*", end=" ")
    print()