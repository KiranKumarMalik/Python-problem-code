# Write a recursion fuction to print the fibonacci value for given positions
def Fibonacci(pos):
    if pos==1 or pos==2:
        return pos-1
    return Fibonacci(pos-1)+Fibonacci(pos-2)
nterm=int(input("Enter number of position upto which we have to display: "))
print(f"Fibonacci squence upto {nterm}th position is {Fibonacci(nterm)}")