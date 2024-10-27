# Inverted left right angled triangle pattern
#  * * * * *
#  * * * * 
#  * * * 
#  * * 
#  * 

row=int(input("Enter the number of row: "))
print('\n'.join(map(lambda val:"* "*val, range(row,0,-1))))