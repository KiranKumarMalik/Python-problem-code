class A:
    var1=4
    var2=5
class B(A):
    var3=9
    var2=6
class C(A):
    var1=1
    var2=3
class D(B,C):
    pass
obj=D()
print(obj.var2)