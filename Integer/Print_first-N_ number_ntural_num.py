# Write a program to print first N natural numbers which are divisible by 2.
numN=int(input('Enter the number of natural number: '))

for ele in range(1,numN+1): # numN is the ending index, upto numN
        if ele %2==0: 
         print(ele)
