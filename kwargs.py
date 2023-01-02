
def userInfo(*args):
    print(type(args))

userInfo()

def userInfo(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}:{value}")


userInfo(username="ferda",password="123",email="ferda@gmail.com",city="istanbul")

def siralama(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(*args)
    print(*kwargs)

siralama(1,2,3,4,5,6,key1="value1",key2="value2")

#kwargs sozluk liste turunde
#args tuple


