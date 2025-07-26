# Pass Or Fail Function :

def POF():
    if(num<35):
        print("Try Next Time.....")
    elif(35<=num<=100):
        print("You Are Pass......")
    else:
        print("Enter The Correct Input : ")
    if 0<=num<=100:

         if(num%2==0):
            print("The Give Input",num, "Its Even")
         else:
            print("The Given Input",num,"Its Odd")

num=int(input("Enter Your Score : "))

POF()
