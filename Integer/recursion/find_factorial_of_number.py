# Factorial of a number using recursion

def Factorial(num):
   if num == 1:
       return num
   else:
       return num*Factorial(num-1)

num = int(input("Enter a number: "))

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print(f"The factorial of 0 is 1")
else:
   print(f"The factorial of {num} is {Factorial(num)}")
