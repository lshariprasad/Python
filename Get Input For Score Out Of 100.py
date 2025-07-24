Score=int(input("Enter Your Score :"))
if(0<Score<35):
    print("Your Score Is Less Than 35, Better Student")
elif(35<Score<70):
    print("Your Score Is ",Score,"Average Student")
elif(70<Score<100):
    print("Your Score Is ",Score,"Great Student")    
else:
    print("Enter The Valid Score....")        
