Mark1 = int(input("Enter Your Firsr Subject  Mark : "))
Mark2 = int(input("Enter Your Second Subject Mark : "))
Mark3 = int(input("Enter Your Third Subject  Mark : "))
Mark4 = int(input("Enter Your Fourth Subject Mark : "))
Mark5 = int(input("Enter Your Fivth Subject  Mark : "))

Total=Mark1 + Mark2 + Mark3 + Mark4 + Mark5

Aveage= Total / 5

if(Aveage<=35):
   print("Your Total Mark Is : ",Total)
   print("You Needed Additional Class Is Required : ",Aveage,"-Percentage")
else:
  print("Your Total Mark Is : ",Total)
  print("You Are Great To Go : ",Aveage,"-Percentage")