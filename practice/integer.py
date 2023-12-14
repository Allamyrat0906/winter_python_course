# sentimeter=int(input("enter sentimeter: "))

# Meter=sentimeter/100
# change=str(Meter)
# new=change.split(".")
# senti=Meter%100

# print(f"{Meter} meter and {senti} senti" )


# # INTEGER 7
# twodigit=int(input("enter number: "))

# onluk=twodigit//10
# birlik=twodigit%10
# sum=onluk+birlik
# product=onluk*birlik

# print("Sum of digits: ",sum)
# print("Product of digits: ",product)


# #INTEGER 10
# a=int(input("enter three digits: "))

# lastd=a%10
# # middle1=a//10
# # middle2=middle1%10

# middle=(a//10)%10

# print("Last digit: ",lastd)
# print("Middle digit: ",middle)



# a=int(input("enter three numbers: "))

# first=a//100
# second=(a//10)%10
# last=a%10

# sum=first+second+last
# multiply=first*second*last

# # print("Sum: ",sum)
# # print("Multiply: ",multiply)

# number=int(input("enter number: "))   # Replace this with your three-digit number

# # Extracting individual digits
# hundreds = number // 100
# tens = (number // 10) % 10
# units = number % 10

# # Swapping tens and hundreds
# swapped_number = tens * 100 +hundreds  * 10 + units

# print("Original number:", number)
# print("Number after swapping digits:", swapped_number)
# a=int(input("enter second: "))

# min=a//3600

# print("full min:", min)

#INTEGER 24

# k=int(input("enter number of day: "))

# # january 1 Monday
# today=k%7

# print("Today:", today)


week=["Sunday","Monday", "Thusday","Wednesday","Thursday","Friday","Saturday"]
k=int(input("enter number of days: "))
today=k%7
print("Today: ", week[today])
