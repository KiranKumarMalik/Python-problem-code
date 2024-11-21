L=[4,1,9,6,1,3]
for ind1 in range(len(L)-1,0,-1):
    for ind2 in range(ind1):
        if L[ind2]>L[ind2+1]:
            L[ind2], L[ind2+1]=L[ind2+1], L[ind2]
print(L)


# ***************** By using user input *****************
# n = int(input("Enter the number of items you want to input: "))
# L = [int(input(f"Enter item {i+1}: ")) for i in range(n)]
# print(f"Original List:{L}")
# for ind1 in range(len(L)-1,0,-1):
#     for ind2 in range(ind1):
#         if L[ind2]>L[ind2+1]:
#             L[ind2],L[ind2+1]=L[ind2+1],L[ind2]
# print(L)