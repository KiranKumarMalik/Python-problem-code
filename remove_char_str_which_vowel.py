# Write a python program to remove the vowels from the string

S="Sarjapur 12#562152 Jspider"
Slst=[]
for ele in S:
    if ele not in 'aeiouAEIOU':
        Slst.append(ele)
print(''.join(Slst))