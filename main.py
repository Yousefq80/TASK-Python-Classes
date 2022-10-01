from unicodedata import name


class Wallet:
    def __init__(self, money=0):
        self.money=money

    def credit(self,amount):
        
        self.money=self.money+amount
        print(f"The total credit is:{self.money}")

    def debit(self,amount):
        
        self.money=self.money-amount
        print(f"The total debit is:{self.money}")

    def __str__(self):
        return f" balance is: {self.money}."
    
# wallet = Wallet(6)
#  wallet = Wallet()  # This should default money inside the wallet to 0
# print(wallet.money)



class Person:
    # Implement the code here
    def __init__(self,name,location,wallet):
                 self.wallet=Wallet(wallet)
                 self.name=name
                 self.location=location
    def moveto(self,point):
        self.point=point
        
        
    

    def __str__(self):
        return f"Mr./Ms:{self.name} your location is {self.location},your balance is:{self.wallet}"

    # def findlocation(self):
        # return 

# person = Person("Moh", 5, 50)


class Vendor(Person):
    # implement Vendor!
    def __init__(self, name, location, wallet=0, range=5, price=2):
        super().__init__(name, location, wallet)
        
        self.range=range
        self.price=price

    def sellto(self, customer, number_of_ice):
        self.customer=customer
        self.number_of_ice= number_of_ice
        
        self.moveto(customer.location)
        s= self.price*self.number_of_ice
    
        customer.wallet.debit(s)
        self.wallet.credit(s)
        # customer.wallet.debit(self.price * self.number_of_ice)
        print(f"{self.number_of_ice} number of ice cream were sold")   
    # def __str__(self):
        print (vendor.name+""+str(vendor.wallet))
# vendor = Vendor("Abdallah", 3, 6)


class Customer(Person):
#     # implement Customer!
    def __init__(self, name, location, wallet):
        super().__init__(name, location, wallet)
    
    def is_in_range (self,vendor):
        self.vendor=vendor
        d=self.location - vendor.location

        if abs(d) <= vendor.range:
            # print(f"the customer within the range",{abs(d)})
           return True
        else:
            # print("the customer not within the range")
           return False
        
    def _have_enough_money(self, vendor, number_of_ice):
        self.vendor=vendor
        self.number_of_ice = number_of_ice
        f_price=vendor.price * number_of_ice
        # print(f"final,{f_price}")
        if self.wallet.money >= f_price:
         print("the customer has enough balance")
         print(self.wallet.money)
         print(vendor.price* number_of_ice)
         return True
        else:
         print("the customer can not purchase.")
         return False

    def request_icecream(self, vendor, number_of_ice):
        self.vendor = vendor
        self.number_of_ice = number_of_ice
        if self.is_in_range(vendor) and self._have_enough_money(vendor,number_of_ice):
         print("request have been made")
         vendor.sellto(customer, number_of_ice)
        else:
         print("the order has been rejected")
        




customer = Customer("Yousef", 2, 30)

vendor = Vendor("H&M.company", 6)

# customer.is_in_range(vendor)
# customer._have_enough_money(vendor,20)
customer.request_icecream(vendor,10)
print(f"{customer.name},{customer.wallet}")
print(f"the vendor,{vendor.name} balance is:,{vendor.wallet}",)
