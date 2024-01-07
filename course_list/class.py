# class MyClass:
#     x = 234

# value=MyClass()

# print(value.x)

# class RealClass:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number


# new = RealClass("Python", 123)
# print(new.name)
# print(new.number)

# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return   f"Hi This is first class  and name: {self.name} {self.age} years old "


# new = Human("Python", 22)
# print(new)


# class UseFunc:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greeting(self):

#         print("hi there " + self.name)

#     def inside(self):
#         p = self.greeting()
#         print(f"{p} and 22 years old ")
#         # print(f"i {self.age} years old")


# new = UseFunc("Python", 33)
# new.inside()


# class google():
#     def __init__(self, name, age, email, ph_number):
#         self.name = name,
#         self.age = age,
#         self.email = email,
#         self.ph_number = ph_number,

#     def costumer(self):
#         costumers = []
#         print("Hi Admin ")
#         coustumers_number = int(
#             input("how many costumer do  you want to add: "))
#         for i in range(coustumers_number):
#             c_name = input("Costumer name:")
#             c_age = int(input("Costumer age:"))
#             c_email = input("Costumer email:")
#             c_phnumber = int(input("Costumer phone number:"))
#             costumers.append(c_name)
#             costumers.append(c_age)
#             costumers.append(c_email)
#             costumers.append(c_phnumber)
#         print(costumers)

# from sys import argv
# script, filename = argv


# class google():
# def costumer(self):
#     costumers = []
#     print("Hi Admin ")
#     coustumers_number = int(
#         input("how many costumer do  you want to add: "))
#     for i in range(coustumers_number):
#         c_name = input("Costumer name:")
#         c_age = int(input("Costumer age:"))
#         c_email = input("Costumer email:")
#         c_phnumber = int(input("Costumer phone number:"))
#         costumers.append(c_name)
#         costumers.append(c_age)
#         costumers.append(c_email)
#         costumers.append(c_phnumber)
#     print(costumers)
#     file = open(filename, "w")
#     n = str(costumers)
#     file.write(n)
# file.close()

#     def service(self):
#         enter = input("Enter service: ")
#         google = {
#             "google_meet": "this servise compinaction people eache other or group contributors",
#             "google_drive": "this servise kepping ouur data to google disk",
#             "google_news": "this servise  news in the world globally",
#             "google_weather": "this servise weather in the world"
#         }
#         print(google[enter])


# new = google()
# # new.costumer()
# new.service()


# class ParentClass():
#     def __init__(self, fname, lname):
#         self.fname = fname,
#         self.lname = lname

#     def printname(self):
#         print(self.fname, self.lname)


# p = ParentClass("Python", "GUI")
# p.printname()


# class Person():
#     def __init__(self, fname, lname):
#         self.fname = fname,
#         self.lname = lname

#     def hello(self):
#         print(self.fname, self.lname)


# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)


# p = Student("Mike", "Tison")
# p.hello()
