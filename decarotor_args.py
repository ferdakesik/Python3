def dec_fn_x2(count):
    def fn_x2(func):
        def wrapper_fn_x2(*args,**kwargs):
            for _ in range(count):
                func(*args,**kwargs)
        return wrapper_fn_x2
    return fn_x2




@dec_fn_x2(count=4)
def selamlama():
    print("merhaba")

@dec_fn_x2(count=2)
def isimle(ad):
    print("merhaba " + ad)

selamlama()
isimle("ferda")