class teacher():
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print("Name ", self.name)
        print("Reg No ",self.regno)

t1=teacher("Sanjay","15")
t2=teacher("Sai Varshini","20")

t1.display()
t2.display()
