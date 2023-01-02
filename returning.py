
def usalma(number):
    #x=usalma(2)
    #y=usalma(3)
    def inner(power):
        return number ** power
    return inner

x= usalma(2)
y= usalma(3)

print(x(3)) #2-3
print(y(2)) #3-3

def islem(islem_adi):
    def toplam(*args):
        toplam=0
        for i in args:
            toplam +=i
        return toplam

    def carpma(*args):
        carpim=1
        for i in args:
            carpim*=i
        return carpim

    if islem_adi=="toplama":
        return toplam
    else:
        return carpma

toplama=islem("toplama")
print(toplama(2,3,4,5))

carpma=islem("carpma")
print(carpma(2,3,2,3))

