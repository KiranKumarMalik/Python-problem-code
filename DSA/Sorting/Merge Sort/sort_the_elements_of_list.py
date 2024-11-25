L=[10,20,23,12,18,20]
left,right=L[:len(L)//2],L[len(L)//2:]
left_ind,right_ind,mind=0,0,0
while left_ind < len(left) and right_ind < len(right):
    if left[left_ind] < right[right_ind]:
        L[mind]=left[left_ind]
        left_ind+=1
    else:
        L[mind]=right[right_ind]
        right_ind+=1
    mind+=1
while left_ind < len(left):
    L[mind]=left[left_ind]
    mind+=1
    left_ind+=1
while right_ind < len(right):
    L[mind]=right[right_ind]
    mind+=1
    right_ind+=1
print(L)