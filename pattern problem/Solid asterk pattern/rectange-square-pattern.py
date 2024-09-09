# To print a rectangle or square pattern using stars
#           * * * * * * *                 * * * * 
#           * * * * * * *       or        * * * *
#           * * * * * * *                 * * * *
#           * * * * * * *                 * * * *
#
#
#

row=int(input("Enter the number of the rows: "))
column=int(input("Enter the number of column: "))

for i in range(row):
    for symbol in range(column): # symbol is the number of "*" symbol upto column
        print("*", end=" ")
    print()