T_count=0
F_count=0
Both_count=0
other_count=0

for i in range (1,100):
    
    if(i%3==0 and i%5==0):
        Both_count+=1
    
    elif(i%3==0):
        T_count+=1
        
    elif(i%5==0):
        F_count+=1
    
    else:
        other_count+=1
       

print("The Given Number Is Divisible By Both 3 and 5...") 
print("The Number Of Both Count Is : ",Both_count)  
print()
print("The Given Number Is Divisible By 3")
print("The Number Of Count Is : ",T_count)
print()
print("The Given Number Is Divisible By 5")
print("The Number Of Count Is :  ",F_count)
print()
print("The Given Number Are Not Divisible By Both 3 and 5...")
print("The Number Of Other Count Is : ",other_count)