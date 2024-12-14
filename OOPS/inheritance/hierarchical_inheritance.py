class Bank():
    def __init__(self,bal):
        self.bal=bal
    def Deposit(self):
        amount=int(input("Enter the deposit amount: "))
        self.bal=self.bal+amount
        print(f"Available Bal is {self.bal}")
class paytm(Bank):
    def __init__(self,bal):
        self.bal=bal
class Phonepe(Bank):
    def __init__(self,bal):
        self.bal=bal
obj=paytm(300)
obj.Deposit()