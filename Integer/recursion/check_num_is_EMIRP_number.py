# Checks if a number is Palindrome using recursion.
def Palindrome(num, rev=0):
    if num == 0:
        return rev
    rev = rev * 10 + num % 10
    return Palindrome(num // 10, rev)

# Checks if a number is prime using recursion.
def Prime(num, val=1):
    if val==num+1:
        return 0
    if num%val==0:
        return 1 + Prime(num,val+1)
    return 0 + Prime(num,val+1)

# Checks if a number is an EMIRP number.
def Emirp(num):
    # Check if the number itself is prime.
    if not Prime(num):
        return False
    
    # Get the reverse of the number.
    reversed_num = Palindrome(num)
    
    # Check if the reversed number is prime and different from the original number.
    if reversed_num != num and Prime(reversed_num):
        return True
    return False

# Example usage
num = int(input("Enter a number: "))
if Emirp(num):
    print(f"{num} is an EMIRP number.")
else:
    print(f"{num} is not an EMIRP number.")
