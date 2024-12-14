class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
class E(B,C):
    pass
class F(D,E):
    pass
print(B.mro()) # mro (method resolving order)