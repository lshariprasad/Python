class dad():
    def phone(self):
        print("Dads Phone")
class mom():
    def sweet(self):
        print("Moms Sweet")

class son(dad,mom):
    def laptop(self):
        print("Son's laptop")

ram=son()
ram.laptop()
ram.phone()
ram.sweet()