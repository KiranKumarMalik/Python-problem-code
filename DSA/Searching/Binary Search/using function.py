def binary_search(L, target):
    least = 0
    high = len(L) - 1
    
    while least <= high:
        ind = (least + high) // 2
        if L[ind] < target:
            least = ind + 1
        elif L[ind] > target:
            high = ind - 1
        elif L[ind] == target:
            return ind  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

L = [3, 5, 7, 8, 31, 333, 420]
target = 31
print(binary_search(L, target))
