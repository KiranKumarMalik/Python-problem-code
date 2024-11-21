# Write a program to find the highest value from the given list
L=[4,9,3,1,7,6]
low=L[0]
for ind in range(1,len(L)):
    if low > L[ind]:
        low=L[ind]
print(low)