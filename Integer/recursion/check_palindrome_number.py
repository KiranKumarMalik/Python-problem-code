def is_palindrome(num, rev=0):
    if num == 0:
        return True if rev == original_num else False
    rev = rev * 10 + num % 10
    return is_palindrome(num // 10, rev)

# Example usage
n = int(input("Enter a number: "))
original_num = n
if is_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")