# implement linear search using for loop
L=[56,42,92,0,5,32,9,92,42]
target=92
for ind in range(len(L)):
    if L[ind]==target:
        print(ind)
        break
else:
    print(-1)