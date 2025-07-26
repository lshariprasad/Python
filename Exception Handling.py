#compile time error

print("Hi")
print("bye")
 
#printt("Hey")       - This called NameError, You gave mistake in printt
print()

#logical Error

a=30
b=20
print(a+b)

#print(a=b)        -This called LogicalError,You sayed that a = b; Its False
print()


#Run Time Error
try:
     a=input("Enter The Value :")
     b=input("Enter The Value : ")
     print(a+b)

except Exception as e:
     print("Something Went Wrong",e)

# string or Float Value will Not be access, Only Integer Number Can Access