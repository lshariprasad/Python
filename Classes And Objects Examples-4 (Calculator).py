class calculator():
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add",self.num1+self.num2)
    def sub(self):
        print("Sub",self.num1-self.num2)
    def multip(self):
        print("Multip",self.num1*self.num2)
    def division(self):
        print("Divison",self.num1/self.num2)


obj1=calculator(10,20)

obj1.add()
obj1.sub()
obj1.multip()
obj1.division()