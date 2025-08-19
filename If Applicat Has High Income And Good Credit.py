# If Applicat Has High Income And Good Credit - Eligible For Loan
# AND : Both Must Be True
# OR  : At Least One
# NOT : 

# AND :
high_income = True
good_credit = True

if high_income and good_credit : 
    print("Eligible For Loan")
else :
    print("You Are Not Eligible For Loan")

# OR :
has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit : 
    print("Eligible For Loan")
else :
    print("You Are Not Eligible For Loan")

# NOT : 
# If Applicat Has High Income And Not Has Criminal Record - Eligible For Loan
has_high_income = True
has_criminal_record = True

if has_high_income and not has_criminal_record : 
    print("Eligible For Loan")
else :
    print("You Are Not Eligible For Loan")
