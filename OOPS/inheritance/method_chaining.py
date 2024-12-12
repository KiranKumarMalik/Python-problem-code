class BankV1:
    def __init__(self, name, mobno):
        self.name = name
        self.mobno = mobno

    def details(self):
        print(f"Name: {self.name}")
        print(f"Mobile No: {self.mobno}")

class BankV2(BankV1):
    def __init__(self, name, mobno, Aadhar, PAN):
        super().__init__(name, mobno)
        self.Aadhar = Aadhar
        self.PAN = PAN

    def details(self):
        super().details()
        print(f"Aadhar No: {self.Aadhar}")
        print(f"PAN: {self.PAN}")

class BankV3(BankV2):
    def __init__(self, name, mobno, Aadhar, PAN, Accno, Bal):
        super().__init__(name, mobno, Aadhar, PAN)
        self.Accno = Accno
        self.Bal = Bal

    def details(self):
        super().details()
        print(f"Account No: {self.Accno}")
        print(f"Balance: {self.Bal}")

# Create an object and call the details method
obj = BankV3("Kiran", 5354646, 169856595659, 'HTEL2486P', 32351868553252, 1000)
obj.details()
