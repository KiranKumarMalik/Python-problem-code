row=int(input("Enter the number of rows: "))
print('\n'.join(map(lambda space,star:"  "*space+"* "*star,range(row-1,-1,-1),range(1,row*2,2))))