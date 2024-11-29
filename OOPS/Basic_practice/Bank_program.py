class Bank:
    Bname='SBI'
    ROI=0.01
    def __init__(self,name,mobno,Aadhar,PAN,Bal):
        self.Name=name
        self.Mobileno=mobno
        self.Aadharno=Aadhar
        self.PAN=PAN
        self.Balance=Bal
    def Balcheck(self):
        print(f"Available Balance:{self.Balance}")
    def deposit(self):
        amount=int(input("Enter the amount to deposit: "))
        if amount <= 20000:
            self.Balance=self.Balance+amount
            print("Amount Credited Successfully...")
            print(f"Available Balance: {self.Balance}")
        else:
            print("Deposit amount upto Rs 20000")
    def withdraw(self):
        amount=int(input("Enter the amount to withdraw: "))
        if amount <= 20000:
            if self.Balance >= amount:
                self.Balance=self.Balance-amount
                print("Amount debited successfully")
                print(f"Available Balance: {self.Balance}")
            else:
                print("Insufficient funds...")
        else:
            print("Withdraw amount upto Rs 20000")

user1=Bank("Kiran",99848644651,1654416466441,"IKGP25469A",5000)
user2=Bank("Chandan",249498449446,56544984944444,"KIOP72478F",3000)
user1.withdraw()
