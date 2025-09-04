
customer = {
    "Name " : "Dev",
    "Age  " : 18,
    "is_verified" : True
}
customer["College"] = "SIMATS"
print(customer["College"])
print(customer.get("birthdate", "Oct 14 2006"))
