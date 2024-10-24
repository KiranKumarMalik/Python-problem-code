def is_palindrome(num, rev=0):
    if num == 0:
        return True if rev == 0 else False
    rev = rev * 10 + num % 10
    return is_palindrome(num // 10, rev) if num != rev else num == rev

# Example usage
n = int(input("Enter a number: "))
if is_palindrome(n):
    print(f"{n} is a palindrome.")
else:
    print(f"{n} is not a palindrome.")
