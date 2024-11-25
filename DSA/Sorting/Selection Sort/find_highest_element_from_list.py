L = [6, 7, 4, 5, 420, 6]
n = len(L)

for ind1 in range(n):
    lind= ind1
    for ind2 in range(ind1 + 1, n):
        if L[ind2] > L[lind]:
            lind = ind2
    L[ind1], L[lind] = L[lind], L[ind1]

print(L[0])