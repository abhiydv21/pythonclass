import time

# start_time = time.time()
# total = 0
# for i in range(1, 100000001):
#     total += 1

# print(total)
# print(time.time() - start_time) 

def execution_time(func):
    def wrapper(*a, **k):
        start_time = time.time()
        func(*a, **k)
        print(time.time() - start_time)
    return wrapper

@execution_time
def example():
    print("Hi everybody, are you fine?")

@execution_time
def example2(n):
    print(f"{n} times")

@execution_time
def example3(x, y):
    print(x + y)

example()
example2(10)
example3(y=10, x = 20)



