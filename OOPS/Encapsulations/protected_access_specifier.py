# Protected access specifiers are created by using single "_" before the data member or method
# We can access protected access specifiers only in a package
# Package: Package is the collection of python module (Python files) with __init__.py
# Library: Library is the collection of Python module

class Mock():
    def __init__(self):
        self._a=200
    def Method(self):
        print(self._a)
obj=Mock()
obj.Method()
print(obj._a)