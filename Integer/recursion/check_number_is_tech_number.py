# Write a recursion function to check wheather a number is a tech number or not 

def is_tech_number(number):
    # Convert the number to a string for easy manipulation of halves
    num_str = str(number)
    
    # Check if the number has an even number of digits
    if len(num_str) % 2 != 0:
        return False

    # Find the midpoint of the number string
    half = len(num_str) // 2
    
    # Split the number into two halves
    left_half = int(num_str[:half])
    right_half = int(num_str[half:])
    
    # Check if the square of the sum of the halves equals the original number
    return (left_half + right_half) ** 2 == number

# Test the function
number = int(input("Enter a number: ")) #2025
print(f"{number} is a Tech number" if is_tech_number(number) else f"{number} is not a Tech number")
