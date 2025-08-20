n = int(input("Enter The Range Of Number : "))

number = []

for count in range (n):
    num = int(input(f"Enter The Number {count+1}:"))
    number.append(num)

print("\nThe Largest Number Is : ",max(number))