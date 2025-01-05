def Sample(a):
    yield a
    a += 20
    yield a
a=30
gobi = Sample(a)
print(next(gobi))
print(next(gobi))
print(next(gobi))