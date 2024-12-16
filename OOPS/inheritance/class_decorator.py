def outer(arg):
    def Inner():
        obj=arg()
    return Inner
@outer
class M17():
    def __init__(self):
        print("Constructor is executed")
M17()