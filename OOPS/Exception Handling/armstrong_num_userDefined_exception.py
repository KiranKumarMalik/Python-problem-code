class Armstrong(Exception):
    def __init__(self, msg):
        self.msg=msg
    def __str__(self):
        return self.msg
try:
    num=int(input("Enter a number: "))
    res=0
    power=len(str(num))
    temp=num
    while num != 0:
        rem=num%10
        res+=rem**power
        num//=10
    if res != temp:
        raise Armstrong(f"{temp} is not an Armstrong Number")
except Armstrong as msg:
    print(f"Error: {msg}")
else:
    print("Armstrong Number")
finally:
    print("Execution Completed")