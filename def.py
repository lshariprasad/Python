# Using Def function:
def great():
    print("welocme to function")

great()

#fucntion with argument:

def great2(name):
    print(f"Hello {name},welcome")


great2("Dev")

#Add Two Numbers:

def add(a,b):
    print(a+b)

add(1, 2)


#Retrun Function :

def add(a,b):
    return a+b

result = add(2, 2)
print(result)


#Add Function Using args:
def add(*args):
    total = 0
    for num in args:
        total += num
        # 0 += 1
        # 1 += 2
        # 3 += 2
    return total

print(add(1,2,3))


#Using **kwargs:
def create_profile(**kwargs):
    print("User Profile")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

create_profile(name= "Dev", age = 19, job ="data engineer")