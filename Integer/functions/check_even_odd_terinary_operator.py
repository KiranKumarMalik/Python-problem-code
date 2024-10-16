#Write a python program to check the number is even or odd using function and terinary operator
def check(num):
    if num%2==0:
        return True
    return False
print("Even number" if check(5) else "Odd number")
