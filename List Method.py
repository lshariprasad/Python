numbers = [14 , 10, 6, 7, 1, 3]
numbers.insert(0,12)  # This Will insert and place the position of a number
numbers.append(18)    # This will add a number in the end
numbers.remove(6)     # This will remove the particular number
numbers.pop()         # This will remove the last number
print(numbers.count(6)) # This Will Count the number of 6, How many times its present 
print(numbers.index(14)) # This Will see the position of a number
numbers.sort()       # ALL the numbers be ascending order
numbers.reverse()    # This will reverse the number in descending order
numbers2 = numbers.copy() # This Will copy the number 1 and will not affect the any numbers 
numbers.append(50) 
print(numbers2)
print(numbers)