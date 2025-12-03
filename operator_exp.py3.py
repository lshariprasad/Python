amount = 1200

tax = amount * 0.18
total = amount + tax

print(total)

if total > 1000 :
    discount = total * 0.10
    total -= discount

print(total)