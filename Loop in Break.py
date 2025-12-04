#Example 1
number = [1,2,3,4,10,6,7,8,9,5]
for i in number:
    if i == 5:
        break
    print(i)

#Example 2

n = [10,-1,0,2,3,8,9,-10,-11,-25,3]

for num in n:
    if num <0:
        continue
    print(num)

#Example 3

n = [10,-1,0,2,3,8,9,-10,-11,-25,3]

for num in n:
    pass # Future Logic Implement

#Example 4

count = int(input("How many numbers do you want? : "))

while count > 0:
    print(f"Countdown : {count}")
    count -= 1

print("Time's Up")

#Example 4

items = []

while True:
    item = input("Add Item (type 'done' to finish): ")

    if item.lower() == "done":
        break

    items.append(item)

print("Items In Cart:", items)
