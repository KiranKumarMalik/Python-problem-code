# 
#    * * * * * * * * *
#      * * * * * * *
#        * * * * *
#          * * *
#            *


row=int(input("Enter the number of rows: "))
print('\n'.join(map(lambda space,star:"  "*space+"* "*star,range(0,row,1),range(row*2-1,0,-2))))