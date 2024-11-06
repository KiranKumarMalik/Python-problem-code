# Write a python code to generate fibonacci sequence using recursion
def Fib(pos):
    if pos==1 or pos==2:
        return pos-1
    return Fib(pos-1) + Fib(pos-2)

def Seq(num):
    if num == pos + 1:
        return
    print(Fib(num))
    Seq(num+1)

num=1
pos=int(input("Enter the position: "))
Seq(num)