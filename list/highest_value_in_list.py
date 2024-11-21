# Write a program to find the highest value from the given list
L=[4,9,3,1,7,6]
high=L[0]
for ind in range(1,len(L)):
    if high < L[ind]:
        high=L[ind]
print(high)