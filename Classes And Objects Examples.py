class Student:
    def __init__(self):
        self.name="DEV"
        self.regno="23"
    def display(self):
        print("Name  : ",self.name)
        print("RegNo : ",self.regno)

S1=Student()
S2=Student()

S1.name="Vijay"
S1.regno="29"

S2.name="Sathish"
S2.regno="22"

S1.display()
print()
S2.display()