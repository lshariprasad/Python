temp=int(input("Enter The Temperatue : "))

if 40 <= temp <= 109:
    print ("It's a Burning Day")
    print ("Take a Unbrella")

elif 11 <= temp <= 39:
    print ("It's a Hot Day")

elif -9 <= temp <= 10:
    print ("It's a Normal Day")

elif -32 <= temp <= -10:
    print ("It's a Cold Day")

elif -50 <= temp <= - 33 : 
    print ("It's a Freez Day")

else : 
    print ("The Given Temperature Is Invalid ")