try:
    Name = str(input("Enter Your Name : "))
    if not Name.isalpha():
        print("The Name Should Contain Only Letters!")
    Age = int(input("Enter You Age : "))
    income = int(input("Enter Your Income : "))
    risk = income / Age
    print(f"\nYou Name is {Name} and Your Age is {Age}")
    print(f"\nYou Can Take Risk Of {risk} This Amount.")
except ZeroDivisionError:
    print("Enter The Valid Age Input")
except ValueError:
    print('Enter The Valid Input ')