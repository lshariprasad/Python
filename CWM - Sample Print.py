
#Using The Range 
course = 'Python For "Beginners"'
print(course[1:0])


# How to Use F - String :

first = 'Dev'
last  = 'Krishna'

message = first + ' [' + last + '] is a coder'

msg = f'{first} [{last}] is a coder'

print(msg)
print(message)



#String Methods

course = 'Python For Beginners'
print(len(course))                            # Length Of The String
print(course[5:15].upper())                   # This Is Used To Make Everything Upper_Case
print(course.lower())                         # This Is Used To Make Everything lower_Case
print(course.find('p'))                       # This Will Find tHe Index Place of A given String 
print(course.replace('For', 'Is Just For'))   # This is Used For to Replace The String
print('Python' in course)                     # This Will Check, The give Word is In Course or Not



#Math Function

x = -2.9

print(round(x))                 # This Will Round The Value Of Decimal Number
print(abs(x))                   # This Will Be Convert Negative Value Into Positive Value


import math

y = 2.5

print(math.ceil(y))             # This is Appled To  (Round-Function)
print(math.floor(y))            # This is round the lower Value of Decimal 
