#
# with open("markalar.txt","a") as file:
#     file.write("\n7-iomi")
#
# with open("markalar.txt") as file:
#     print(file.read())

with open("markalar.txt","r+") as file:
    markalar =file.read()
    markalar ="1-samsung\n" +markalar
    file.seek(0)
    file.write(markalar)

with open("markalar.txt") as file:
    print(file.read())