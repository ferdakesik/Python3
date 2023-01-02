
def fn_x2(func):
    def wrapper_fn_x2(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)

    return wrapper_fn_x2

@fn_x2
def selamlama():
    print("merhaba")

@fn_x2
def isimle(ad):
    print("merhaba " + ad)

selamlama()
isimle("ferda")


