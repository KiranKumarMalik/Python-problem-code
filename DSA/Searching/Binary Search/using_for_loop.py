L = [3, 5, 7, 8, 31, 333, 420]
target = 420
least = 0
high = len(L) - 1

for ind in range(len(L)):
    ind = (least + high) // 2
    if L[ind] < target:
        least = ind + 1
    elif L[ind] > target:
        high = ind - 1
    elif L[ind] == target:
        print(ind)
        break
else:
    print(-1)
