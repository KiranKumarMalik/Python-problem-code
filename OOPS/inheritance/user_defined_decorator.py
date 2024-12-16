def outer(arg):
    def Inner():
        print("Hello")
        arg()
    return Inner
@outer
def Sunday():
    print("We will attend")
Sunday()