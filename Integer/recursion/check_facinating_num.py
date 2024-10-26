# Write a recursion function to check the number is facinating number or not

def is_fascinating_number(num):
    # Base case: Number must have at least three digits to be fascinating
    if num < 100:
        return False
    
    # Concatenate number, number*2, and number*3 into one string
    concatenated = str(num) + str(num * 2) + str(num * 3)
    
    # Recursive helper function to check if the concatenated string contains all digits from 1 to 9
    def check_digits(concatenated, digit=1):
        # Base case: If digit is greater than 9, all digits 1 to 9 are present
        if digit > 9:
            return True
        # Check if the current digit is present in the concatenated string
        if str(digit) not in concatenated:
            return False
        # Recursive call for the next digit
        return check_digits(concatenated, digit + 1)

    # Ensure the length of the concatenated string is 9 and contains all digits 1 to 9
    return len(concatenated) == 9 and check_digits(concatenated)

# Test the function
number = int(input("Enter a number: ")) #192
print(f"{number} is a fascinating number" if is_fascinating_number(number) else f"{number} is not a fascinating number")
