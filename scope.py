#scope kavram fondkyonlarda


a="global deger"

def fn1():
    a = "local deger"
    print(a)

fn1()
print(a)

#------------------
#global
city="sitanbul"

def changeCity(new_city):
    # local
    city=new_city
changeCity("bursa")
print(city)

#------------------
#ic ice fonksiyonda en ic fonksiyon gelir
city="istanbul"

def dis_fonskyon():
    city="izmir"

    def ic_fonksiyon():
        city="ankara"
        print("ic fonksiyon " + city)

    ic_fonksiyon()
    print(city)
dis_fonskyon()
print(city)

#-------------
a=10
def fn2():
    global a #if you do global , o da degisiyor icerde
    #print(f"a : {a}")

    a=20
    print(f"cnahge a to {a}")
fn2()
print(a)






