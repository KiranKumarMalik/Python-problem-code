def SingleTonclass(arg):
    L=[]
    def Inner():
        if len(L)==0:
            obj=arg()
            L.append(obj)
        return L[0]
    return Inner
@SingleTonclass
class movie1():
    def __init__(self):
        self.maxticket=100
    def Booking(self):
        print(f"Available Tickets are {self.maxticket}")
        reqticket=int(input("Enter the number of tickets: "))
        if reqticket <= self.maxticket:
            print("Ticket booked successfully...")
            self.maxticket -= reqticket
        else:
            print("Ticket not available")

@SingleTonclass
class movie2():
    def __init__(self):
        self.maxticket=100
    def Booking(self):
        print(f"Available Tickets are {self.maxticket}")
        reqticket=int(input("Enter the number of tickets: "))
        if reqticket <= self.maxticket:
            print("Ticket booked successfully...")
            self.maxticket -= reqticket
        else:
            print("Ticket not available")

@SingleTonclass
class movie3():
    def __init__(self):
        self.maxticket=100
    def Booking(self):
        print(f"Available Tickets are {self.maxticket}")
        reqticket=int(input("Enter the number of tickets: "))
        if reqticket <= self.maxticket:
            print("Ticket booked successfully...")
            self.maxticket -= reqticket
        else:
            print("Ticket not available")

def BookMyShow():
    print("1. Movie 1 \n2. Movie 2 \n3. Movie 3")
    option=int(input("Choose the movie options"))
    if option==1:
        user=movie1()
        user.Booking()
    elif option==2:
        user=movie2()
        user.Booking()
    elif option==3:
        user=movie3()
        user.Booking()
    else:
        print("No movie available")

def Paytm():
    print("1. Movie 1 \n2. Movie 2 \n3. Movie 3")
    option=int(input("Choose the movie options"))
    if option==1:
        user=movie1()
        user.Booking()
    elif option==2:
        user=movie2()
        user.Booking()
    elif option==3:
        user=movie3()
        user.Booking()
    else:
        print("No movie available")

BookMyShow()
print("-----------------------")
Paytm()
print("-----------------------")
BookMyShow()
