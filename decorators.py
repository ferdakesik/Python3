
def selamlama(fn):
    def inner(ad):
        print("programa hos geldiniz")
        fn(ad)
        print("gorusmek uzere")
    return inner

@selamlama
def gunaydin(ad):

    print("gunaydin " + ad)


@selamlama
def iyigunler(ad):

    print("iyi gunler " + ad)

@selamlama
def iyiaksamlar(ad):

    print("iyi aksamlar " + ad)

gunaydin("ali")
iyiaksamlar("veli")
iyigunler("asye")

