class grandpa():
    def phone(self):
        print("Grandpa Phone")

class dad(grandpa):
    def money(self):
        print("Dads Money")

class son(dad):
    def laptop(self):
        print("Son's Laptop")

ram=son()

ram.laptop()
ram.money()

d1=dad()
d1.phone()

ram.phone()