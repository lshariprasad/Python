name = " Beru "
name += "is my name "
print(name)
print("dev".upper())
print("DEV".lower())
print(abs(-5.5))
print(round(5.9))
print()


#list 
dogs = ["Dev" , 2 , "syd" , True , "Quincy " , 7]
dogs[2] = "Dev"
dogs.append("Hello Bro")
dogs.extend(["Memo",6])
dogs += [ "San" , 205]
dogs.remove("Dev")
print(dogs)
print(dogs[:3])
items = [ "Sat" , "Cream" , "Key", "Yuv"]
items.sort()
print(items)
print()

#tuples
name = ("roger" , "syd")
name[-1]
name.index("roger")
len(name)
print("roger" in name)
print(sorted(name))
newtuple = name + ( " Tina " , " Quincy")

#Dictionaries
Cat={"name" : "roger" , "age" : 8}
Cat["name"] = "Syd"
print(Cat)
print()


#Function
def Hello(name , age):
    print("Hello " + name + ", You are " + str(age) + " Years Old!" )
Hello ( "Dev" , 19)
print()

#Loops
count=0
while count < 10:
    print("Money")
    count += 1
print("Only Do it Now")



























