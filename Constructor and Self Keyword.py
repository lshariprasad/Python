class laptop:
    price="0"
    ram=""
    def __init__(self):  #Its In-build Function. (Constructor())
        self.ram=""
        self.processor=""
        print("Demo")
    def display(self):
        print("ram : ",self.ram)
        print("Processor : ",self.processor)


hp=laptop()
hp.price=50000
hp.ram="16gb"
hp.processor ="I5"


dell=laptop()
dell.ram="8gb"
dell.processor="i7"


print(hp.price)
print(hp.ram)
print(hp.processor)
print()

hp.display()
dell.display()