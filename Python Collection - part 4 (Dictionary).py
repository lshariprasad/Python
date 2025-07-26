a={
    "name"    :"Dev",
    "age"      :"18",
    "location" :"Chennai",
    "student"  :{"bala","sathish","vijay"}
    }

print(a)
print()


print(a["name"])
print()


print(a.keys()) # This Will Show Left Side Of keys struture
print()


print(a.values()) # This will show right side of value
print()

a["color"]="red" # we can add like this dictionary keywords on it
print(a)
print()

a.update({"age":2}) # this will update the structure
print(a)
print()

a.pop("age") # We can use pop commend To deleted the age
print(a)

del a["location"] # We can use del commend to deleted the location
print(a)

#  del a   # This Command Is Used To Deleted The Entire Structure

# a.clear  # This Command Is used to clear entire Structure
