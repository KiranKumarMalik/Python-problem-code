 # Write a python program to print only uppercase vowels from the string
S=str(input("Enter a string: "))
res=''
for ch in S:
    if ch in "AEIOU":
        res=res+ch
print(f"Uppercase letter of {S} is {res}")