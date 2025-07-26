class Vehicle():
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    def start(self):
        print("Car started")

C1=Vehicle()
C1.start()

print()

C2=Car()
C2.start()

