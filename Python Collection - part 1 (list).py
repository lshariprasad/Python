a=[1,2,3,4,5,6]
print(a)
print()
#index Always Starts From 0 1 2 3 4 5 .....


num=int(input("Enter A Number : ")) #Getting Input form User 

a.append(num) # Num is Add in the List
print()

a.append(True) # We Can add String Without Colon


a.append("Dev") #We can Include String Also


a.append(6) # We can Add Number Also


print(a) # This Will Print {a} Values
print()

print(a[1]) # This Will Print The Placing Of {a} which we given position
print()

a.insert(0,9) #Since, 0 is The Position and 9 is The Value We Add on the List


print(a)
print()


a[2]=13 # We can Replace The Number In That Position

print(a)
print()

a.pop(2) # This Pop command is used to remove The particular number or String of the given position form list 

a.pop() #This POP command is used to remove the last element or last String


print(a)
print()


b=[1,2,3,4,5,6]        # This Is (b) List
c=[11,22,33,44,55,66]  # This Is (c) List

b.extend(c)  # This Extend Command Is Used Merge Two List Together

c.extend(b)  # This Extend Command Is Used Merge Two List Together

print(b) #  This Will Print B to C
print()

print(c) #  This Will Print C to B
print()