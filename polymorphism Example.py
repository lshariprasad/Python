class Animal():
    def sound(self):
        print("Animal Makes Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Braks")

class Bird(Animal):
    def sound(self):
        print("Bird Sings")

A1=Animal()
A1.sound()

A2=Dog()
A2.sound()

A3=Bird()
A3.sound()