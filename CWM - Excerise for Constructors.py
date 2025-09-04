class Person():

    def name(self):
        self.name = input("Enter You Name : ")
    
    def talk(self):
        self.talk = input("Enter Your Talking Language : ")

    def introduction(self):
        print(f'Hello, I am {self.name} and I Know To Speak {self.talk}')


person1 = Person()
person1.name()
person1.talk()
person1.introduction()