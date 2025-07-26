num=int(input("Enter The Factorial Number : "))
factorial = 1
i=1

if(num<0):
    print("The Given Number Is In Negative : ",num)
else:
    while(i<=num):
        factorial = factorial * i
        i = i + 1
    print("The Factorial ",num,"Value Is ",factorial)