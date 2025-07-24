salary=int(input("Enter Your Salary : "))
age=int(input("Enter Your Age : "))

if(salary>=20000 or 18<=age<=25):
    loanamount=int(input("Enter Your Loan Amount : "))
    if(loanamount<=50000):
        print("You are Eligible For Loan.... Thankyou")
    else:
        print("You are Amount Is Higher Than Your Limits....")
else:
    print("You are Not Eligible For Loan... Thank You")

  