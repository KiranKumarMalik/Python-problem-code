# Write a Python program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x) 
# otherwise (x, x) if the number is odd.

StartInt=int(input("Enter the starting integer number: "))
EndInt=int(input("Enter the ending integer number: "))
res_dict={}
for k in range(StartInt,EndInt+1):
    if k % 2 == 0:   
        res_dict[k]=k**2   # square of the number, if the number is even K=1 then value=1*1=1 and K=4 then value=4*2=16
    else:
        res_dict[k]=k
print(res_dict)