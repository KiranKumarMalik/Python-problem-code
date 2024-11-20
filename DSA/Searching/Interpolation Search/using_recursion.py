def Interpolation(L,target,low,high):
    if L[low]>target or L[high]<target or low>high:
        return -1
    ind=int(low+((high-low)/(L[high]-L[low]))*(target-L[low]))
    if L[ind]<target:
        return Interpolation(L,target,ind+1,high)
    elif L[ind]>target:
        return Interpolation(L,target,low,ind-1)
    elif L[ind]==target:
        return ind

L=[3,5,7,8,31,333]
target=8
print(Interpolation(L,target,0,len(L)-1))