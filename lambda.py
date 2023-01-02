
def us_alma(a):
    return a ** 2
print(us_alma(3))


# lambda arguments : expression

sonuc = (lambda a: a ** 2)(2) #desgijkene atayip oyle cagrio

print(sonuc)


us_alma = lambda a:a**2
sonuc=us_alma(6)
print(sonuc)


toplama = lambda a,b,c : a+b+c
sonuc = toplama(5,8,12)
print(sonuc)

tersCevir=lambda x: x[::-1]
sonuc=tersCevir("ferda kesik")
print(sonuc)


def fn1(n):
    return lambda a: a ** n

us_alma2 =fn1(2)
sonuc=us_alma2(3)
print(sonuc)




