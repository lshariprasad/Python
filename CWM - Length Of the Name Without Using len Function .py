name = input ( "Enter Your Name : ")

# Instant Of Using len:

count = 0
for char in name:
    count +=1


if count <= 2:
    print (" Name Must Be At Least 3 Characters")

elif count >=50 :
    print ("Name Can Be A Maximum Of 50 Characters ")

else:
    print ("Name Looks Good!")
