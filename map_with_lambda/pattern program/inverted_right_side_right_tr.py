# Inverted left right angled triangle pattern
#   * * * * * 
#     * * * * 
#       * * * 
#         * * 
#           * 

row=int(input("Enter the number of row: "))
print('\n'.join(map(lambda space,star:"  "*space+"* "*star, range(0,row+1),range(row,0,-1))))