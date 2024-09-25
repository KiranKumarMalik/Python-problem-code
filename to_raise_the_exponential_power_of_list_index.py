# Write a Python program to raise the elements of a list to the power of their respective index.

lst=[2,5,7,6]
exp=0
result=[]
for i in range(len(lst)):
    exp=lst[i]**i
    result.append(exp)
print(result)