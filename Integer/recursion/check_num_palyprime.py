# Write a recursion function to check the number is Paliprime number or not

# Checks if a number is Palindrome using recursion.
def Palindrome(num,rev=0):
    if num == 0:
        return 0
    rev = rev * 10 + num % 10
    return Palindrome(num // 10, rev) if num != rev else num == rev

# Checks if a number is prime using recursion.
def Prime(num, val=1):
    if val==num+1:
        return 0
    if num%val==0:
        return 1 + Prime(num,val+1)
    return 0 + Prime(num,val+1)

def Palyprime(num):
    if Palindrome(num) and Prime(num):
        return True
    return False

num = int(input("Enter a number: "))  
if Palyprime(num):
    print(f"{num} is a Paliprime number.")
else:
    print(f"{num} is not a Paliprime number.")