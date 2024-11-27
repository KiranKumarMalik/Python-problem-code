def divide(L):
    if len(L) <= 1:
        return L
    # Split the list into two halves
    mid = len(L) // 2
    left,right = L[:mid],L[mid:]
    
    # Recursively divide the halves
    divide(left),divide(right)
    
    # Merge the sorted halves back into L
    merge(L, left, right)

def merge(L, left, right):
    left_ind, right_ind, middle_ind = 0, 0, 0
    
    # Merge the two sorted lists
    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] < right[right_ind]:
            L[middle_ind] = left[left_ind]
            left_ind += 1
        else:
            L[middle_ind] = right[right_ind]
            right_ind += 1
        middle_ind += 1
    
    # Copy any remaining elements from the left half
    while left_ind < len(left):
        L[middle_ind] = left[left_ind]
        middle_ind += 1
        left_ind += 1
    
    # Copy any remaining elements from the right half
    while right_ind < len(right):
        L[middle_ind] = right[right_ind]
        middle_ind += 1
        right_ind += 1

# Test the code
L = [11, 6, 18, -7, 14, 0, -4]
divide(L)
print(L)


# def divide(L):
#     if len(L) <= 1:
#         return L
#     # Split the list into two halves
#     mid = len(L) // 2
#     left,right = L[:mid],L[mid:]
    
#     # Recursively divide the halves
#     divide(left),divide(right)
    
#     # Merge the sorted halves back into L
#     merge(L, left, right)

# def merge(L, left, right):
#     left_ind, right_ind, middle_ind = 0, 0, 0
    
#     # Merge the two sorted lists
#     while left_ind < len(left) and right_ind < len(right):
#         if left[left_ind] < right[right_ind]:
#             L[middle_ind] = left[left_ind]
#             left_ind += 1
#         else:
#             L[middle_ind] = right[right_ind]
#             right_ind += 1
#         middle_ind += 1
    
#     # Copy any remaining elements from the left half
#     while left_ind < len(left):
#         L[middle_ind] = left[left_ind]
#         middle_ind += 1
#         left_ind += 1
    
#     # Copy any remaining elements from the right half
#     while right_ind < len(right):
#         L[middle_ind] = right[right_ind]
#         middle_ind += 1
#         right_ind += 1

# # Test the code
# n = int(input("Enter the number of items you want to input: "))
# L = [int(input(f"Enter item {i+1}: ")) for i in range(n)]
# print(f"Original List:{L}")
# divide(L)
# print(f"Sorted list: {L}")
