# implement linear search using function
def linear(L,target):
    for ind in range(len(L)):
        if L[ind]==target:
            return ind
    else:
        return -1

L=[43,32,69,0,32,9,43]
target=43
print(linear(L,target))