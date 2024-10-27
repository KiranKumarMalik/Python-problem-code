# Backward right angled trinagle pattern
#        *
#      * *
#    * * *
#  * * * *

row=int(input("Enter the number of row: "))
print('\n'.join(map(lambda space,star:"  "*space+"* "*star, range(row-1,-1,-1),range(1,row+1))))