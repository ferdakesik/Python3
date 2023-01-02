
# def adin_ne():
#     ad = input("adini soyle: ")
#     return ad
#
# #adin_ne()
#
# print("sisteme hosgeldiniz",adin_ne())


# def topla():
#     return 20+30
#
# sonuc = topla()
#
# print(sonuc)

saat = 15

def selamla():
    if (saat<12):
        return "gunaydin"
    elif (saat>=12) and (saat<18):
        return "iyi gunler"
    else:
        return "iyi aksamlar"

sonuc = selamla() + ", Levent"
print(sonuc)







