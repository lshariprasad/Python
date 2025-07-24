number=int(input("Enter The Number : "))
if(number%3==0 and number % 5 == 0):
   print("Its Divisible By Both 3 and 5")
elif(number%3==0):
   print("Its Divisible By 3")
elif(number%5==0):   
   print("Its Divisible By 5")
else:
   print("This Number Is Not Divisible By 3 Or 5")