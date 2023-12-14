# data type

# number=45
# double=45.22
# text="second python lesson"
# boolean=True

# print(type(number))
# print(type(double))
# print(type(text))
# print(type(boolean))

# changing type

# double=45.22
# number=4

# change=int(double)
# changetofloat=float(number)

# print(change)
# print(changetofloat)

# sn1="45"
# sn2="5"

# cn1=int(sn1)
# cn2=int(sn2)

# sum=cn1+cn2
# result=sn1+sn2

# print(sum)
# print(result)

# text="""
# example
# example
# example
# example
# example
# example
# example
# example
# example
# example
# """
# print(text)


# text="Python"

# print(text[0])
# print(len(text))

# sometext="Python is cool" 

# test=("day" in sometext)
# print(test)

# text="Python , JavaScript"

# print(text.replace("P","H"))
# print(text.split(","))


# text1="hello "
# text2="world"
# new=text1+text2

# print(new)

# age=22

# text="I {} years old"

# print(text.format(age))
# new=f"I {age} years old"
# print(new)

# ESCAPE

# text="We are the so-called \"Vikings\" from the north."
# print(text)

# text="python is cool an easy way to learn"
# new=text.count("is","we")
# print(new)

#boolean
# print(bool(False))
# print(bool(None))
# print(bool(1))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))


# operator
# num1=5
# num2=10

# sum=num1+num2
# subt=num2-num1
# multy=num1*num2
# dev=num2/num1

# print(sum)
# print(subt)
# print(multy)
# print(dev)

num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))


power=num1**num2

result=f"{num2} power of {num1} => {power}"

print(result)