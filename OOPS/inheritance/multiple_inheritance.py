class Father:
    def money(self):
        print("No money")
        return 0

class Mother:
    def money(self):
        print('Go and study')

class Child(Father, Mother):
    def money(self):
        amount = int(input("Enter the amount we have: "))
        if amount < 150:
            if Father.money(self) == 0:  # Call Father's money method
                Mother.money(self)  # Call Mother's money method explicitly
        else:
            print(f"Amount: {amount}")

# Create an object and call the method
obj = Child()
obj.money()