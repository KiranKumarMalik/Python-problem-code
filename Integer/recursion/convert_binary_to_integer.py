# Write a recursion function to convert binary number to integer number
def ConvertToInteger(binary_str):
    """Converts a binary string to decimal using recursion."""
    if not binary_str:
        return 0
    return int(binary_str[-1]) + 2 * ConvertToInteger(binary_str[:-1])

binary_str = str(input("Enter a binary number: "))
print(f"The integer value of {binary_str} is {ConvertToInteger(binary_str)}") 