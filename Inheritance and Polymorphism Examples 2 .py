class person():
    def __init__(self,name):
        print("")
        self.name=name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade

    def display(self):
        print(self.name,self.grade)

s1=student("John","A")
s1.display()        
    