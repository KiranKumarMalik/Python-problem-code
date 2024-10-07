# Write a python program to filter the digit of string and store it into a list
 
S="Sarjapur 12#562152 Jspider"
new=[]
for i in S:
   if i.isdigit(): # Checked the digit is availabe in the string
      new.append(i)
print(new)