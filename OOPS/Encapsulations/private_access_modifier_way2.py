# getter(): This method is used to access the private data members or private method outside the class
# setter(): This method is used to modify the private data members
 
class Mock():
    def __init__(self):
        self.__a=200
    def getter(self):
        return self.__a
    def setter(self):
        self.__a=int(input("Enter a value: "))
obj=Mock()
print(obj.getter())
obj.setter()
print(obj.getter())
