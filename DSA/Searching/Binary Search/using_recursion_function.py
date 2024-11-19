def binary_search(L, target, least, high):
    if least > high:  # Base case: target not found
        return -1
    
    ind = (least + high) // 2
    if L[ind] == target:  # Base case: target found
        return ind
    elif L[ind] < target:  # Search in the right half
        return binary_search(L, target, ind + 1, high)
    else:  # Search in the left half
        return binary_search(L, target, least, ind - 1)


L = [3, 5, 7, 8, 31, 333, 420]
target = 420
result = binary_search(L, target, 0, len(L) - 1)
print(result)
