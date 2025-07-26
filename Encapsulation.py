class company():
    def __init__(self):               # When Single Underscore is protect
        self._companyName="DEV"      # When Double Underscore is private 
    
    def companyname(self):            #This will become private
        print(self._companyName)

class b(company):
    pass

b1=b()
print(b1._companyName)
