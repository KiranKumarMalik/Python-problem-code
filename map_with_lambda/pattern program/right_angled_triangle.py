# Right angled trinagle pattern using map and lambda function
#     *
#     * * 
#     * * *
#     * * * *

row=int(input("Enter the number of row: "))
print('\n'.join(map(lambda val:"* "*val, range(1,row+1))))