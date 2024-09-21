S=str(input("Enter the string: "))

even_str=[]
odd_str=[]
sum=0
for i in range(len(S)):
    if i % 2==0:
        sum=sum+i
        even_str.append(S[i])
    else:
        odd_str.append(S[i])

print(f"Even number index elements: {even_str}")
print(f"Sum of even index elements: {sum}")
print(f"Odd number index elements: {odd_str}")