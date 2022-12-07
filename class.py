class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def difference(self):
        return self.num1 - self.num2

    def product(self):
        return self.num1 * self.num2 

    @staticmethod
    def sqrt(num):
        return num**0.5

c = Calculator(20,10) 
print(c.add())
print(c.difference())
print(c.product())
print(Calculator.sqrt(25))
