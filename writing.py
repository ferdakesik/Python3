#"r" : read okuma
#"w" : write yazma


with open("info.txt","w",encoding="UTF-8") as file:
    file.write("levent\n")
    file.write("ferda\n")
    print(file)


with open("info.txt") as file:
    print(file.read())