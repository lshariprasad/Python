#First Example
name = input("Enter Your Name : ")
age  = int(input("Enter Your Age : "))
patient = input("Did The Patient is New Or Old : ")

print(" We check in a patient named",name,"." )
print(" He's", age, "years old and is a",patient,"patient. \n")


#Second Example
person = input("Enter Your Full_Name  : ")
color  = input("Enter Your Favorite_Color : ")

print(person + " likes " + color + "\n")

#Third Example
birth_year = int(input("Enter Your Birth Year : "))
current_year = int(input("Enter The Current Year : "))

age = current_year - birth_year

print("Your Age Is : ",age)



#Fourth Example
#To convert lbs to kg, multiply the given lbs value by 0.45359237 kg. 

pound = input("Enter Your Pound Weight (lbs) : ")

CPTK = float(pound) * 0.45359237 #CPTK - Convert Pound Into Kilogram...

print("Weight In Kilograms : ",CPTK)
