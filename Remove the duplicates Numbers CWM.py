#Remove the duplicates Numbers

numbers = [2, 2, 6, 5, 9, 9, 6, 5, 3]
uniques = []
for i in numbers:
    if i not in uniques:
        uniques.append(i)
uniques.sort()
print(uniques)
