# import random
# new=random.randrange(15,20)

# print(new)

# #IF 1
# number=int(input("give integer number: "))

# if number >0 :
#     number=number+1
#     #number +=1
#     print("result: ",number)
# else:
#     print("result: ",number)


# num=int(input('=>'))
# if num > 0:
#     num+=1
#     print('== ',num)
# elif num<0:
#     num-=2
#     print('== ',num)

# else:
#     print('10')

# A = int(input("Hay do: "))

# if A>0:
#     A+=1
# else:
#     A-=2
# print(A)
# a=int(input("enter a digit: "))
# b=int(input("enter b digit: "))
# c=int(input("enter c digit: "))

# pos=0
# neg=0

# if a>0:
#     pos+=1
# else:
#     neg+=1
# if b>0:
#     pos+=1
# else:
#     neg+=1
# if c>0:
#     pos+=1
# else:
#     neg+=1
# print("Posetive number : ", pos)
# print("Negarive number : ", neg)

# Given three numbers
# num1 = 15
# num2 = 8
# num3 = 21

# # Finding minimum
# if num1 <= num2 and num1 <= num3:
#     minimum = num1
# elif num2 <= num1 and num2 <= num3:
#     minimum = num2
# else:
#     minimum = num3

# # Finding maximum
# if num1 >= num2 and num1 >= num3:
#     maximum = num1
# elif num2 >= num1 and num2 >= num3:
#     maximum = num2
# else:
#     maximum = num3

# # Finding the value between minimum and maximum
# if (num1 != minimum) and (num1 != maximum):
#     middle_value = num1
# elif (num2 != minimum) and (num2 != maximum):
#     middle_value = num2
# else:
#     middle_value = num3

# print("The value between the minimum and maximum is:", middle_value)

import random

print("wellcome the door game!!!!!!")
print("choose the door inside 3 doors")
print("""
        1. door 1
        2. door 2
        3. door 3
""")
print("hint you just select (number of doors)")
select_door=int(input("selecting door =>  "))


if select_door==1:
    print("welcome the guessing game!!!")
    print("""
        game explanation enter number between (1 and 10)
        and  if you gues the my numbers you will win!!!     
            """)
    your_number=int(input("my number: "))
    random_number=random.randrange(1,10)

    if your_number==random_number:
        print("yeeee you won!!!!")
       
    else:
        print("ow nooo you lose!!!!")
        print("computer number ",random_number)

if select_door == 2:
    print("""
        You selected the second door to continue you must know the capital of the country  
        the countries 
    """)
    countries = {
        "Turkmenistan":"Ashgabat",
        "Usa":"Washington Dc",
        "Pakistan":"Islamabad",
        "Afganistan":"Kabul",
        "France":"Paris"
    }
    # new=["Turkmenistan" ,....]
    r = random.randrange(1,5)
    li = list(countries.keys())
    li2 = list(countries.values())
    print("You must know the capital of ",li[r])
    ans = input("enter the capital :  ")
    if li2[r] == ans:
        print("Congratulations you are good at geography ")
    else:
        print("I'm sorry you quit the game")