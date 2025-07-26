s_username = "DEV"
s_password = "1410"

username=input("Enter The UserName : ")
password=input("Enter The PassWord : ")

def Validate():
    if(s_username == username and s_password == password):
        return True
    else:
        return False


a=Validate()
print(a)