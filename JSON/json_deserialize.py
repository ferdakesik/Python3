
import json
with open("user.json") as file:
   # data=file.read()
    data=json.load(file)
   # print(data)
    #print(type(data))

    print(data["userName"])
    print(data["hobbies"][2])


#json-string
data="""
{
  "userName" : "leventert",
  "firsName" : "Levent",
  "lastName": "ertune",
  "email": "ertuna@gmail.com",
  "hobbies": ["kitap","kalem","silgi"],
  "age": 38
}

"""

data=json.loads(data)
print(data)
print(data["hobbies"])
