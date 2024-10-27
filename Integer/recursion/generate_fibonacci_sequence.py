# Write a recursion function to generate fibonacci sequences
def Fibonacci(pos):
    # Base cases
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    # Recursive case
    return Fibonacci(pos - 1) + Fibonacci(pos - 2)

nterm = int(input("Enter the number of terms: "))

if nterm <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:", end=" ")
    for i in range(nterm):
        print(Fibonacci(i), end=" ")