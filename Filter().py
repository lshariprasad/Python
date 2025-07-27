

numbers= [ 1,2,3,4,5,6,7,8,9,10]

def isEven(n):
    return n % 2 == 0

#lambda n : n % 2 == 0  --- isEven

result = filter (isEven , numbers)

print(list(result))