num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    gcd = num2  # Set gcd to the smaller number
else:
    gcd = num1

while True:
    if num1 % gcd == 0 and num2 % gcd == 0:
        print(f"The GCD is: {gcd}")
        break
    gcd -= 1  # Decrement by 1 to check the next smaller number
