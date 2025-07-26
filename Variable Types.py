class phone():
    chargetype="C-Type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand : ",self.brand)
        print("Price : ",self.price)
        print("ChargeType : ",self.chargetype)
        

samsung = phone("Samsung","100000")
samsung.display()

print()

Nokia = phone("Nokia","21000")
Nokia.display()