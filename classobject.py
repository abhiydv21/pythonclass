#1. Class and Object
#2. Inheritance
#3. Abstraction
#4. Polymorphism

#Noun -> object
# adjective -> property, Characteristics
#nverb -> method, function, action

class Student: 

    def __init__(self, _id, roll_no, name, gender):
        self._id = _id
        self.roll_number = roll_no
        self.name = name
        self.gender = gender
        self.total_attendance = 0

    def view_attendance(self):
        return f"Total attendance of {self.name} is {self.total_attendance}"
        
class ProductPriceError(Exception):
    pass

class Product:

    def __init__(self, name, sku, price):
        self.name = name
        self.sku = sku
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ProductPriceError("Price can not be smaller than zero")
        self.__price = price

tshirt = Product("T-shirt", "123", 500)
print(tshirt.__dict__)
try:
    tshirt.price = -200
except ProductPriceError as err:
    print(err)
# tshirt.price = -200
print(tshirt.__dict__)

    
          


