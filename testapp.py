import sys

if len(sys.argv) == 2:
    print("Usage: python email_generator.py <Full Name and Last Name>")
    sys.exit()

full_name = " ".join(sys.argv[1:])
print(full_name)


#Format the name
email = full_name.lower().replace(" ", ".") + "@company.com"

#Output
print("\n ---- Your Profile ----")
print("Full Name : ",full_name)
print("Generated Email : ",email)
