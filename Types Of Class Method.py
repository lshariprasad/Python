class laptop():
    chagetype = "C Type"
    def __init__(self):
        self.brand=""
        self.price="34"

    def setPrice (self,price):
        self.price=price
    
    def getPrice(self):
        print(self.price)


    @classmethod                                # class Method
    def changeChagetype(cls):
        cls.chargetype="B Type"
        print("Charger Type Changed To B")

    @staticmethod                               #staticmethod
    def info():
        print("This Is Laptop Class")

hp=laptop()
hp.setPrice(200000)
hp.getPrice()

laptop.changeChagetype()

hp.info()