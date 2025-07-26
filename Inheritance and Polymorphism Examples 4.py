class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,salary, department):
        super().__init__(name,salary)
        self.department=department

    def display(self):
        print("Name : ",self.name)
        print("Salary : ",self.salary)
        print("Department :",self.department)

m1=Manager("Dev",5000000,"EEE")
m1.display()