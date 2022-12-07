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



students_score = [
    {"name": "Ram", "score":80},
    {"name": "Sita", "score":100},
    {"name": "Hari", "score":35},
    {"name": "John", "score":40},
    {"name": "Rita", "score":36},
    {"name": "Rio", "score":90},
    {"name": "Jose", "score":50},
]
out = []
for i in students_score:
    score = (i.get("score"))
    if score >= 40:
        out.append(i)

print(out)

output = list(filter(lambda i:i.get("score") >= 40, students_score))
print(output) 


 
