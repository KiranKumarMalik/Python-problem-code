# Write a program to check the number is Even number or Odd number
def check(num):
    if num%2==0:
        return f"{num} is an Even number"
    else:
        return f"{num} is an Odd number"
print(check(5))