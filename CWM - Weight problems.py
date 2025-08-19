weight = float(input("Enter Your Weight : "))
unit = input("Convet to (L) for pounds or (K) for kilos: ").upper()

if unit == "L":
    converted = weight / 0.45359237 #kg to Pounds
    print("Weight In Pounds Is  : ",converted)

elif unit == "K":
    converted = weight * 0.45359237 #Pounds to Kg
    print("Weight In Kilos: ",converted)

else :
    print ("You Enter The Wrong Input......")
