class chennai:
    name=""
    drink=""
    def Job(self):
        print("Lets Find a Job")
    def Bussiness(self):
        print("Start a new Bussiness")

Krishna = chennai()
Ramesh  = chennai()

Ramesh.name="ramesh"
Krishna.name="Krishna"

Ramesh.drink="Yes"
Krishna.drink="No"


print("Name : ",Ramesh.name)
print("Drinks : ",Ramesh.drink)
Ramesh.Job()
print()


print("Name",Krishna.name)
print("Drinks : ",Krishna.drink)
Ramesh.Bussiness()