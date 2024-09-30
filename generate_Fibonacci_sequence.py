# Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.
# Example
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# a=0, b=1 then c=a+b, d=b+c, e=c+d, f=d+e, g=e+f, h=f+g, i=g+h, j=h+i, k=i+j, l=j+k, m=k+l, n=l+m, ...

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms?: "))

# first two terms
n1=0
n2=1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
