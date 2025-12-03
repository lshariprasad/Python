#Example 1
drive_name = "Hari"

print(drive_name.lower())
print(drive_name.upper())
print(drive_name.capitalize())

#Example 2
mobile = "9962466372"

masked = mobile[:2] +"******" + mobile[-2:]

print(masked)

# Example 3
song = "SHApe OF YoU"
artist = "Dev"

formatter = f"{song.title()} - {artist.title()}"
print(formatter)

#Example 4
location = "chennai center"

fixed_location = location.replace( "chennai center","Mangadu")
print(fixed_location)

#Split Method
message = "Your uber Booking id is :UB123456. Please Keep it Safe"
# Method - 1
booking_id = message.split(":")[1]
New_Booking_id = booking_id.split(".")[0]
print(New_Booking_id)

#Method - 2
booking_id = message.split(":")[1].split(".")[0]
print(booking_id)

#Example 5

Discount = "Zomato100%"
Offer = input("Enter Discount Offer : ")

if Discount == Offer:
    promo_msg = "use " + Discount + " to get 100 off on your first order"

    if Offer in promo_msg:
        print("Offer Applied")
    else:
        print("Not Offer")
else:
    print("Coupon Code Is Invalid")

#Example 6

feedback = "the driver was polite and the ride was smooth"
print("position is : ", feedback.find("polite"))

name = "Deva Krishna"
initials = "".join ([word[0].upper() for word in name.split()])
print(initials)

dierty_input = "   airport   "
clean=dierty_input.strip()
print(clean)

word1 = "The Trip was amazing and the car was clean"
word_count = len(word1.split())
print(word_count)