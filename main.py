from unicodedata import name


class Wallet:
    def __init__(self, money=0):
        self.money=money

    def credit(self,amount):
        self.amount=amount
        self.money=self.amount+self.money
        print(f"The total amount is:{self.money}")

    def debit(self,amount):
        self.amount=amount
        self.money=self.amount-self.money
        print(f"The total amount is:{self.money}")

wallet = Wallet(6)
wallet = Wallet()  # This should default money inside the wallet to 0
print(wallet)


class Person:
    # Implement the code here
    def __init__(self,name,location,wallet,moveto):
                self.name=name
                self.location=location
                self.walllet=wallet
                self.moveto=moveto


person = Person("Moh", 5, 50)


class Vendor(person):
    # implement Vendor!
    def __init__(self,name,location,range=5,price=1,sellto=0):
         super().__init__(name,location)
         self.range=range
         self.price=price
         self.sellto=sellto

vendor = Vendor("Abdallah", 3, 6)


class Customer:
    # implement Customer!
    pass


customer = Customer("Abdallah", 3, 6)
