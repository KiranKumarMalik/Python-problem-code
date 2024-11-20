L=[3,5,7,8,31,333,420]
target=333
low=0
high=len(L)-1
while low<=high and L[low]<=target<=L[high]:
    ind=int(low+((high-low)/(L[high]-L[low]))*(target-L[low]))
    if L[ind]<target:
        low=ind+1
    elif L[ind]>target:
        high=ind-1
    elif L[ind]==target:
        print(ind)
        break
else:
    print(-1)