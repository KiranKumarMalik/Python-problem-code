# By default all the data members are public access specifiers
# We can access public access specifiers anywhere in the program
 
class Mock():
    def __init__(self,a):
        self.a=a
    def Method(self):
        print(self.a)
obj=Mock(6)
print(obj.a)
obj.Method()
Mock.Method(obj)