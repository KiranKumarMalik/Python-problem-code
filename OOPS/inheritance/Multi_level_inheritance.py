class A():
    var1=20
    var2=9
class B(A):
    var1=0
    var4=420
class C(B):
    var5=11
    var2=15
obj=C()
print(obj.var2)