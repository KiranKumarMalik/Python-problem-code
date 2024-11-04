# Count the number of vowels present in a string

S=str(input("Enter a string: "))
res=''
count=0
for ch in S:
    if ch in "aeiouAEIOU":
        count=count+1
print(f"Number of vowels present in {S} is {count}")