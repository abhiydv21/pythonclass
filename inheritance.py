class Person:
    def __init__(self, name, address):
        self.name = name 
        self.address = address

    def walk(self):
        print(f"{self.name} is walking.")

class Teacher(Person):
    def __init__(self,name,address,designation):
        super().__init__(name,address)
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching.")

class Student(Person):
    def __init__(self, name, address, roll_number):
        super().__init__(name, address)
        self.roll = roll_number
        
    def walk(self):
        print(f"{self.name} is running.")

s = Student("Hari", "Ktm", 2)
s.walk()

t = Teacher("Ram", "Ktm", "prof")
t.walk()
t.teach()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# class Person(User):
#     def __init__(self, username, password, name, address):
#         super().__init__(username, password)
#         self.name = name
#         self.address = address

#     def profile(self):
#         print(f"Name: {self.name}")
#         print(f"Address: {self.address}")
#         print(f"Username: {self.username}")


# class Student(Person):
#     def __init__(self, username, password, name, address, rollno):
#         super().__init__(username, password, name, address)
#         self.roll_number = rollno

#     def profile(self):
#         super().profile()
#         print(f"Roll number: {self.roll_number}")


# class Teacher(Person):
#     def __init__(self, username, password, name, address, designation):
#         super().__init__(username, password, name, address)
#         self.designation = designation

#     def profile(self):
#         super().profile()
#         print(f"Designation: {self.designation}")

# s = Student ("ram@gmail.com", "324", "Ram", "Ktm", 2)
# s.profile()

# t = Teacher("hari@gamil.com", "564", "Hari", "Baneshwor", "prof")
# t.profile()



class ProductPriceError(Exception):
    pass

class Product:
    def __init__(self, name, price):
        self.name = name 
        self.__price = price 

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ProductPriceError("Price cannot be less than zero.")
        self.__price = price

tshirt = Product("Tshirt", 500)
try:
    tshirt.price = -100
    print(f"Without exception: {tshirt.price}")
except ProductPriceError as msg:
    print(msg)
    print(f"After Exception: {tshirt.price}")
