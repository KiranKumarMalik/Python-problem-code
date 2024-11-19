# implement linear search using while loop
L=[56,42,92,0,5,32,9,92,42]
target=92
ind=0
while ind != len(L):
    if L[ind]==target:
        print(ind)
        break
    ind=ind+1
else:
    print(-1)