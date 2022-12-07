#exception handling
#try:
#   # code
except Exception: # catch specific error or exception
    #code
except Exception: #catch specific error or exception

try:
    a = int("Enter num1: ")
    b = int("Enter num2: ")
except valueerror:
    print("can not conver to integer")
else:    
    print(a + b)

name = input("Enter name: ")
finally:
    print("code is executed ")
    
