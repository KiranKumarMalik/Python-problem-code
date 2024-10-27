# Write a python program to find the factorial of the range elements
def Factorial(num,fact=1):
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(list(map(Factorial,range(5,11))))

# def Factorial(num,fact=1):
#     for i in range(1,num+1):
#         fact=fact*i
#     return fact
# factorialObj=map(Factorial,range(5,11))
# for fact in factorialObj:
#     print(fact)