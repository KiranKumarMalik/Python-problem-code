# Write a program to print following pattern

#                 *
#                * *
#              * * * *
#            * * * * * *
#          * * * * * * * *


row=int(input("Enter the number of rows: "))
print('\n'.join(map(lambda space,star:" "*space+"*"*star,range(row,-1,-1),range(1,))))