def Interpolation(L,target,low,high):
    while low <= high and L[low <= target <= L[high]]:
        ind=int(low+((high-low)/(L[high]-L[low]))*(target-L[low]))
        if L[ind]<target:
            low=ind+1
        elif L[ind]>target:
            high=ind-1
        elif L[ind]==target:
            return ind
    return -1

L=[3,5,7,8,31,333,420]
target=333
print(Interpolation(L,target,0,len(L)-1))