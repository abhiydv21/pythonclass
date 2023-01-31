# a = {
#     "properties":{
#         "profile":{
#             "name": "ram",
#             "education":[
#                 {"college": "abc", "year": 2018}
#                 {"college": "xyz", "year": 2020}
#             ]
#         },
#         "followers": 10000
#         "following": 100
#     }
# }

# name = a.get("properties").get("profile").get("name")
# followers = a.get("propertoes").grt("followers")
# following = a.get("properties").get("following")
# print(f"Name: {name.capitalize()}")
# print(f"Followers: {followers}")
# print(f"Following: {following}")
# education = a.get("properties").get("profile").get("education")
# for education in education:
#     college = education.get("college")
#     year = education.get("year")
#     print(f"Education({year}): {college.upper()}")
#     exit()


#     #############################################################

# #  oil_prices = [
# #     {
# #         "oil_type":"petrol"
# #         "prices":[
# #             {"year": 2018, "price": 100},
# #             {"year": 2019, "price": 150},
# #             {"year": 2020, "price": 180},
# #         ]
# #     },
# #     {
# #         "oil_type": "diesel",
# #         "prices":[
# #             {"year": 2018, "price": 80}
# #             {"year": 2019, "price": 100}
# #             {"year": 2020, "price": 160}
# #         ]
# #     }
# #  ]  
 
# #  for oil in oil prices:
# #     print(f"Oil Type:{oil.get('oil_type').capitalize()}")
# #     prices = oil.get("prices")
# #     total_prices = 0
# #     for price in prices:
# #         year = price.get('year')
# #         p = price.get('price')
# #         total_price = total_price + p 
# #         print(f"Price({year}): Rs.{p}")



# students_score = [
#     {"name": "Ram", "score":80},
#     {"name": "Sita", "score":100},
#     {"name": "Hari", "score":35},
#     {"name": "John", "score":40},
#     {"name": "Rita", "score":36},
#     {"name": "Rio", "score":90},
#     {"name": "Jose", "score":50},
# ]
# out = []
# for i in students_score:
#     score = (i.get("score"))
#     if score >= 40:
#         out.append(i)

# print(out)

# output = list(filter(lambda i:i.get("score") >= 40, students_score))
# print(output) 


# colors = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]
# remove = ["yellow", "red"]
# #remove these colors from remove list
# for i in colors:
    

# colors = ["yellow", "red", "green", "blue", "yellow", "orange", "red"]
# # take user input input two times which color to be removed
  

profile = {
    "name" : "Ram",
    "gender" : "Male",
    "education" : [
        {"college": "ABC college", "level": "+2" },
        {"college": "XYZ College", "level": "bachelor"},
    ],
    "addresses":[
        {
            "temporary": {
                "ward": 1,
                "city": "Kathmandu",
            },
            "permanent": {
                "ward": 2,
                "city": "Kavre",
            }
        }
    ]
}

# print(f"Name: {profile.get('name')}")
# print(f"Gender: {profile.get('gender')}")

# educations = profile.get("education")
# for education in educations:
#     print(f"College: {education.get('college')} and Level: {education.get('level')}")

# addresses = profile.get("address")
# for address in addresses:

#     print(f"Temporary: {address.get('temporary')}, ")
#     print(f"Permanent: {address.get('permanent')} ") 
    





students = {
    "count": 2,
    "data": [
        {
            "name": "Ram",
            "address": "Tinkune",
            "course": "Python Django",
            "attendance": [
                {
                    "month": "January",
                    "total_working_days": 25,
                    "present": 24,
                    "absent": 1,
                    "leave": 0,
                },
                {
                    "month": "February",
                    "total_working_days": 28,
                    "present": 20,
                    "absent": 2,
                    "leave": 6,
                }
            ]
        },
        {
            "name": "Hari",
            "address": "Tinkune",
            "course": "Python Django",
            "attendance":[
                {
                    "month": "January",
                    "total_working_days": 25,
                    "present": 23,
                    "absent": 1,
                    "leave": 1,
                },
                {
                    "month": "February",
                    "total_working_days": 28,
                    "present": 27,
                    "absent": 0,
                    "leave": 1,
                }
            ]
        }
    ]
}


students = students.get("data")
for student in students:
    students_attendance = students.get("attendance")
    

