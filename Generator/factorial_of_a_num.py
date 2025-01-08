def factorial(num):
    if num >= 0:
        yield 1
    fact = 1
    for val in range(1, num + 1):
        fact *= val
        yield fact
genObj = factorial(5)
while True:
    print(next(genObj))