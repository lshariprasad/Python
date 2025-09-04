class Mammal():
    def walk(self):
        print("I Love To Walk Slowly...")

class Dog(Mammal):
    def bit(self):
        print("I Love To Bit That Person :) ")

class Cat(Dog):
    def sleeply(self):
        print("I Love To Sleeeeeeep.... Don't Disturb Me")

animals1 = Cat()
animals1.bit()

animals2 = Dog()
animals2.walk()