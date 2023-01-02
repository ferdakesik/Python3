
# file=open("text.txt")
# file.close()

with open("text.txt") as file:
    print(file.read())

print(file.close())