# cars={
#     "nissan":"N12",
#     "BMW":"X5",
#     "Toyoto":"Y5",
# }


# turkmen_en={
#     "apple":"alma",
#     "orange":"pyrtykal",
#     "limon":"limonsary"
# }

# print(turkmen_en["apple"])

# cars_order={
#     1:"BMW",
#     2:"Y5",
#     3:"AMG",
#     4:"FORD",
#     5:"NISSAN"
# }
# number=int(input("Number of cars: "))
# print(cars_order[number])
# print(len(cars_order))

# money_type={
#     "USA":"$",
#     "TKM":"TMT",
#     "TURKIE":"L",
#     "JAPAN":["YUAN","$"]
# }

# print(money_type["JAPAN"])

# money_type={
#     "USA":"$",
#     "TKM":"TMT",
#     "TURKIE":"L",
#     "JAPAN":["YUAN","$"]
# }
# # print(money_type.get("USA"))
# # print(money_type.keys())
# # print(money_type.values())
# # money_type.keys()

# # money_type["TKM"]="$"
# money_type.update({"TURKIE":"LLL"})
# money_type.popitem()
# print(money_type["TURKIE"])
# print(money_type)
# registration={
#     "user1":{
#         "name":"John",
#         "age":16
#     },
#     "user2":{
#         "name":"Mark",
#         "age":23
#     }
# }

# print(registration["user1"]["name"])


translate={
    "apple":"alma",
    "orange":"pyrtykal"
}
turkmen=[]
english=[]
turkmen=turkmen+list(translate.values())
english=english+list(translate.keys())
print("English: ", english)
print("Turkmen: ", turkmen)