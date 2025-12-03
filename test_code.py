#L - E - G - B
from statistics import quantiles


#L

def order():
    food = "Curd Rice"
    print("your order is :",food)

order()

#E

def card():
    discount = 10 #E

    def checkout():
        print("applying discount :", discount)

    checkout()

card()


#G

user_id = "HARI PRASAD"

def homepage():
    print("Welcome : ", user_id)

def profile():
    print("Welcome to the profile page: ", user_id)

homepage()
profile()


#B

print(__file__)

#All Variables

devliery_partner = "swiggy"

def hotel():
    item = "pizza"

    def order_now():
        quantily = 2
        print(f"ordering {quantily} {item} using {devliery_partner}")
    order_now()

hotel()
