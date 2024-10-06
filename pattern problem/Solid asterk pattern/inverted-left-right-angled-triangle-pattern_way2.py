# Inverted left right angled triangle pattern
#  * * * * *
#  * * * * 
#  * * * 
#  * * 
#  * 

num=int(input("Enter the number of row: ")) 
for row in range(num,0,-1):
    for col in range(row):
        print('*', end=' ')
    print()