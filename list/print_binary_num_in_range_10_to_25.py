# Write a program to print the binary numbers from given range:
StartInd=int(input("Enter starting range: "))
EndInd=int(input("Enter Ending range: "))
for num in range(StartInd, EndInd+1):
    n = num  # Copy of the number to convert to binary
    binary = ""  # Initialize an empty string for the binary representation

    # Convert decimal to binary
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    print(f"{num} in binary is: {binary}")