def sum_of_two_numbers(num1, num2):
    total = num1 + num2
    return total

total_sum = sum_of_two_numbers(10, 15)
print(total_sum)

def profile(name,address,contact):
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"contact: {contact}")

profile("Ram", "Ktm", "98547623") 
print("--------------------------------")
profile("Ram", "98547623", "ktm")

print("----------------------------------")


def total_sum(num1,num2):
    total = num1 + num2
    print(f"Total: {total}")

def total_sum_two(num1, num2):
    total = num1 + num2
    return total 

b = total_sum(10, 15)
print(f"b: {b}")
a = total_sum_two(10,15)
print(f"a: {a}")
exit()
