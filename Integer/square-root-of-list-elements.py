lst=[]
n=int(input("Enter the length of the list: "))

for i in range(n):
    elements=int(input("Enter the elements "+ str(i+1)+": ")) # str(i+1) is used to print the number of the element
    lst.append(elements)
print("The list is:", lst)

square_root=[]
for i in lst:
    square_root.append(i**0.5)
print("The square root of the elements in the list is:", square_root)
