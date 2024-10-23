# Python program to display the Fibonacci sequence
def fibonacci(nterms):
   if nterms <= 1:
       return nterms
   else:
       return(fibonacci(nterms-1) + fibonacci(nterms-2))

nterms = int(input("Enter the number of terms: "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:",end=" ")
   for i in range(nterms):
       print(fibonacci(i),end=" ")