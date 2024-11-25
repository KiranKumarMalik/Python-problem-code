L=[6,7,4,5,420,6]
least=0
ind1=0
for ind1 in range(len(L)-1):
    lind=ind1
    for ind2 in range(ind1+1,len(L)):
        if L[lind]>L[ind2]:
            lind=ind2
    L[ind1],L[lind]=L[lind],L[ind1]
print(L)


# n = int(input("Enter the number of items you want to input: "))
# L = [int(input(f"Enter item {i+1}: ")) for i in range(n)]
# least=0
# ind1=0
# for ind1 in range(len(L)-1):
#     lind=ind1
#     for ind2 in range(ind1+1,len(L)):
#         if L[lind]>L[ind2]:
#             lind=ind2
#     L[ind1],L[lind]=L[lind],L[ind1]
# print(L)