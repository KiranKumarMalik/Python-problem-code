# These are created by giving double "__" before the data members or method
# We can access private access modifier only inside the class

class Mock():
    def __init__(self):
        self.__a=200
    def Method(self):
        print(self.__a)
obj=Mock()
obj.Method()