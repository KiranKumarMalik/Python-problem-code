class parent():
    var1=100
    var2=200
    def properties(self):
        print('100 Cr')
class child(parent):
    var2=300
    var3=400
    def converts(self):
        print('1000 Cr')
obj1=child()
obj1.properties()