# from sys import argv
# script, filename = argv
# print(f"We're going to erase {filename}")
# print("If you don't want that  hit CTR-C (^C)")
# print("If you want that hit RETURN")
# input("?")
# print("Opening the file...")
# target=open(filename, 'w')
# print("Turnacating the file... Godbye!")
# target.truncate()
# print("Now I am going to ask you for three lines")
# line1=input("line 1: " )
# line2=input("line 2: " )
# line3=input("line 3: " )
# print("I am going to write these  to the file")
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
# print("And finally we close it ")
# target.close()





from sys import argv
script,filename=argv

print("Food save system")
howmany=int(input("how many data add: "))
file=open(filename ,"w")
for i in range(howmany):
    data_v=input("enter your data: ")
    file.write(data_v)
    file.write("\n")

print("all done")
file.close()