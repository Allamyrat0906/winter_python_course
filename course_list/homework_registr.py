from sys import argv
script, filename = argv

print("Welcome to registration service!!!!!")
how_many_registred = int(input("How many registered: "))
file = open(filename, "w")
for i in range(how_many_registred):
    # id
    id = (input("ID: "))
    if id.isalpha():
        print("id must be a number")
        break
    else:
        pass
    # name
    name = str(input("Name: "))
    if name.isalpha():
        pass
    else:
        print("name must be a string")
        break
    # course
    Course = str(input("Course: "))
    if Course.isalpha():
        pass
    else:
        print("Course must be a string")
        break
    # duration
    duration = (input("Duration: "))
    if duration.isalpha():
        print("duration must be a number")
        break
    else:
        pass
    # cprice
    c_price = (input("Courses price: "))
    if c_price.isalpha():
        print("c_price must be a number")
        break
    else:
        pass
    # phnumber
    ph_num = (input("Phone number: "))
    if ph_num.isdigit():
        pass
    else:
        print("phone number must be number ")
        break

    txt_id = f"Registration ID: {str(id)}\t  |"
    txt_name = f"User Name: {name}\t  |"
    txt_course = f"Course Name: {Course}\t   |"
    txt_duration = f"Course Duration: {str(duration) } month\t   |"
    txt_price = f"Course Price: {str(c_price)} TMT\t   |"
    txt_ph_num = f"Phone Number: +993{str(ph_num)}\n"

    file.write(txt_id)
    file.write(txt_name)
    file.write(txt_course)
    file.write(txt_duration)
    file.write(txt_price)
    file.write(txt_ph_num)
print("Successfully Registered!")
file.close()
