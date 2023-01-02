import json
user={
  "userName" : "leventert",
  "firsName" : "Levent",
  "lastName": "ertune",
  "email": "ertuna@gmail.com",
  "hobbies": ["kitap","kalem","silgi"],
  "age": 38
}


#print(user["userName"])

result=json.dumps(user,indent=2)
print(result)
#print(result)
print(type(result))

with open("user.json","w") as file:
    json.dump(user,file)