# cars=["BMW","FORD","TOYOTA","AMG"]

# print(cars)
# print(len(cars))

#data types in array

# numbers=[1,2,3,4,5,6,7,8,9,10]
# string=["Python","Java","JavaScript"]
# boolean=[True,False]

# mix=["Python",22,True]

# print(numbers)
# print("------------------------------")
# print(string)
# print("------------------------------")
# print(boolean)
# print("------------------------------")
# print(mix)
# print("------------------------------")
# print(type(string))

# CONVERTING

# fruits=("apple", "orange","banana")
# convert_to_list=list(fruits)
# print(type(convert_to_list))


# ACSESS DATA
# food=["apple",  "orange","banana" ,"watermelon"]
# print(food[0])
# print(food[1])
# print(food[-1])
# print(food[2:3])
# print(food[-1:-2])
# print(food[:3])
# print(food[1:])

#changing value
# food=["apple",  "orange","banana" ,"watermelon"]
# drink=("juice","water","beer")
# food[0]="cherry"
# food.insert(2,"granad")
# print(food)
# food.append("cherry")
# food.extend(drink)
# food.remove("apple")
# food.pop()
# food.clear()
# for i in range(len(food)):
#     print(food[i])
# food.sort(reverse=True)
# food.reverse()
# new=food+(drink)
# print(new)

# print("Welcome to Bootcamp registration form")
# student=[]
# name=input("Enter your name: ")
# surname=input("Enter your surname: ")
# student.append(name)
# student.append(surname)

# print(student)

# digits=["","one" ,"two" ,"three" ,"four" ,"five" ,"six" ,"seven" ,"eight" ,"nine"]
# tens=["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety","hundred"]

# number=int(input("enter number between (10 to 100):  "))

# digitsn=number%10
# tensn=number//10

# print(tens[tensn] , "-",digits[digitsn])



print("Welcome to Bootcamp registration!!")
numberpeople=int(input("how many peaple add"))
students=[]

for i in range(numberpeople):
    name=input("enter name : ")
    students.append(name)
print(students)



