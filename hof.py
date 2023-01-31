#map, #filter
#lambda

# a = lambda x,y:x * y
# print(a(10, 20))

# map(func, iterable_object)
# a= [2, 9, 7, 16, 54,86]

# b=[]
# for i in a:
#     b.append(i+1)

# print(b)

# def increase_by_one(n):
#     return n + 1

# output = list(map(increase_by_one, a))
# print(output)

# name_list = ["ram", "shyam", "sita", "meera", "hari"]

# output = (list(map(lambda name:name.capitalize(), name_list)))
# print(output)

# output = list(map(str.capitalize, name_list))
# print(output)



# filter(func, iterable_object)
# this function should always return boolean value

# a= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# out = list(filter(lambda n:n % 2 == 0, a))
# print(out)

# a = "2,4,6,d,8,9,e,4"
# num_list = a.split(",")
# numbers = filter(str.isdigit, num_list)
# print(sum(map(int, numbers)))

# print(sum(map(int, filter(str.isdigit,a.split(",")))))



marks_of_students = [
    {
        "name": "Ram",
        "marks":
        {"maths": 80, "science": 85, "computer": 90},
    },
    {
        "name": "Sita",
        "marks":{"maths": 87, "science": 79, "computer": 85},
    },
    {
        "name": "Hari",
        "marks":{"maths": 90, "science": 75, "computer": 88},
    },
]

for m in marks_of_students:
    print(m.get("name"))
    print(sum(m.get("marks").values()))


  