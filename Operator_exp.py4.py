age = int(input("Enter Your Age: "))
student = str(input("Are You Student (Yes / No ): ")).strip().lower()


if age >= 60 or student == "yes" : # This is a Condition Block
    print("Yes Discount")
else :
    print("No Discount")

