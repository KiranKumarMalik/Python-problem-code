class parent:
    var1=100
    var2=200
class child(parent):
    var2=300
    var3=400
obj=child()
print(obj.var1)