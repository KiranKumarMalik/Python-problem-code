# implement linear search using recurssion function
def linear(L,target,ind=0):
    if ind==len(L):
        return -1
    if L[ind]==target:
        return ind
    return linear(L,target,ind+1)

L=[43,33,69,0,32,9,43]
target=43
print(linear(L,target))