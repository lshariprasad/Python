#Example 1
age = int(input("Enter your age: "))

if age >= 18:
    print("You Can Vote")
else:
    print("You Cant Vote")

has_licsense = str(input("Did You Have Licsense (Yes / No) :" ))

if age >= 18:
    if has_licsense == "Yes":
        print("You can Drive")
    else :
        print("Go and Take License")
else:
    print("You Are Too Young To Drive")

#Example 2

marks = int(input("Enter Your Marks:"))

if marks >= 90:
    print("Grade : A")
elif marks >= 80:
    print("Grade : B")
elif marks >= 70:
    print("Grade : C")
elif marks >= 60:
    print("Grade : D")
elif marks >= 50:
    print("Grade : E")
else:
    print("Grade : F")

#Example 3

order_amount = int(input("Enter Your Order Amount:"))
days = ("sat")
membership = str(input("Do you Live Gold Membership (Yes / No) :" ))

if (order_amount >= 1000 and days in ["sat","sun"]) or membership == "Yes":
    print("20% discount")
else:
    print("No discount")
