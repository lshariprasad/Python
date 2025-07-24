print("Min Calculate For 2 Number")
a=int(input("Enter The First Number  : "))
b=int(input("Enter The Second Number : "))

z=input(("Enter The Symbol You Need : Add , Sub , Mul , Div : "))
Add=a+b
Sub=a-b
Mul=a*b
Div=a/b

if(z=="Add"):
    print("The Addation Of Two Numbers Are : ",Add)
elif(z=="Sub"):
    print("The Subraction of Two Number Are : ",Sub)
elif(z=="Mul"):
    print("The Multiple Of Two Number Are : ",Mul)
elif(z=="Div"):
   print("The Division Of Two Number Are : ",Div)
else:
   print("Invalid Operation")